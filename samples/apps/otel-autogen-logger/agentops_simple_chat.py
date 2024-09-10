import os
from autogen import ConversableAgent, UserProxyAgent
from autogen import ConversableAgent, UserProxyAgent, config_list_from_json
import autogen.runtime_logging
import agentops
from dotenv import load_dotenv


def main():
    # Load LLM inference endpoints from an env variable or a file
    # See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    # and OAI_CONFIG_LIST_sample.
    # For example, if you have created a OAI_CONFIG_LIST file in the current working directory, that file will be used.
    load_dotenv()
    AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # When initializing AgentOps, you can pass in optional tags to help filter sessions
    agentops.init(AGENTOPS_API_KEY, default_tags=["simple-autogen-example"])

    # config_list = config_list_from_json(env_or_file="./OAI_CONFIG_LIST.json")
    config_list = [{
        "model": "gpt-4",
        "api_type": "azure",
        "api_key": OPENAI_API_KEY,
        "base_url": "https://observability-spikes-oai.openai.azure.com/",
        "api_version": "2024-02-01"
    }]

    # Create the agent that uses the LLM.
    assistant = ConversableAgent(
        "agent", llm_config={"config_list": config_list})

    # Create the agent that represents the user in the conversation.
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    # Let the assistant start the conversation.  It will end when the user types exit.
    assistant.initiate_chat(user_proxy, message="How can I help you today?")

    # Close your AgentOps session to indicate that it completed.
    agentops.end_session("Success")
    print("Success! Visit your AgentOps dashboard to see the replay")


if __name__ == "__main__":
    main()
