from autogen import ConversableAgent, UserProxyAgent, config_list_from_json
import autogen.runtime_logging
from otel_logger import OtelLogger
from dotenv import load_dotenv
import os
import json


def main():
    # Load LLM inference endpoints from an env variable or a file
    # See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    # and OAI_CONFIG_LIST_sample.
    # For example, if you have created a OAI_CONFIG_LIST file in the current working directory, that file will be used.

    # Intialize the Autogen logger
    autogen.runtime_logging.start(logger=OtelLogger())

    load_dotenv()
    AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # config_list = config_list_from_json(env_or_file="./OAI_CONFIG_LIST.json")
    config_list = [{
        "model": "gpt-4",
        "api_type": "azure",
        "api_key": OPENAI_API_KEY,
        "base_url": "https://observability-spikes-oai.openai.azure.com/",
        "api_version": "2024-02-01"
    }]

    # config_list = config_list_from_json(env_or_file="./OAI_CONFIG_LIST.json")

    with autogen.runtime_logging.autogen_logger.tracer.start_as_current_span(
            "workflow_run") as current_span:
        # Create the agent that uses the LLM.
        assistant = ConversableAgent(
            "agent", llm_config={"config_list": config_list})

        # Create the agent that represents the user in the conversation.
        user_proxy = UserProxyAgent("user", code_execution_config=False)

        # Let the assistant start the conversation.  It will end when the user types exit.
        response = assistant.initiate_chat(
            user_proxy, message="How can I help you today?")
        current_span.set_attribute(
            "messages", json.dumps(response.chat_history))

    autogen.runtime_logging.stop()


if __name__ == "__main__":
    main()
