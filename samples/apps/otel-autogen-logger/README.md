# Monitoring Autogen Application with Azure Monitor and OpenTelemetry

This example demonstrates how to use the OpenTelemetry SDK to instrument Autogen application and send telemetry data to Azure Monitor.


## Instrumentation Details

| Instrumentation | Description |
|-----------------|-------------|
| [Auto Studio and SDK ](./../../../autogen/logger/otel_logger.py) | Added new logger to core Autogen SDK. This will enable `autogen.runtime_logging.start(logger_type="otel", config={})`(TODO: Create UpStream PR)   |
| [OTel Logger](./otel_logger.py) | Overriding Baselogger by implementing BaseLogger abstraction. This can be used without the upstream changes to AutoGen SDK |

## Demo Prerequisites
- Clone the repository(https://github.com/sudivate/autogen/tree/sudivate/otel-playground) and checkout branch `sudivate/otel-playground`
- Open the project in Visual Studio Code and reopen the project in the devcontainer(studio) VS code will prompt you to do this
- Rename the `env.example` file to `.env` and update the values for AZURE_APPINSIGHTS_CONNECTION_STRING and AZURE_OPENAI_API_KEY
- Install required dependencies by running `pip install -r ./samples/apps/otel-autogen-logger/requirements.txt`
- Add  below debug configuration in the `.vscode/launch.json` file
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
        "name":"Python Debugger: Current File",
        "type":"debugpy",
        "request":"launch",
        "program":"${file}",
        "console":"integratedTerminal",
        "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "Python Debugger: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "samples.apps.autogen-studio.autogenstudio.web.app:app",
                "--port=8081",
                "--reload"
            ],
            "jinja": true,
            "envFile": "${workspaceFolder}/.env"
        }
        ,

    ]
}
```


## AutoGen Studio Workflow Demo

This demo demonstrates how to use the AutoGen Studio to create a workflow that uses Azure Open AI to plan a trip. The workflow is triggered by a user request to plan a trip. The workflow uses Azure Open AI to generate a travel plan based on the user's preferences. The workflow then sends the travel plan to the user.

- Run vscode debugger with the configuration `Python Debugger: FastAPI`
- Open the browser and navigate to `http://localhost:8081/` You should see the Autogen Studio UI
- Configure the inbuilt Travel planning Workflow with Azure Open AI and run the workflow in new session

## AutoGen SDK Demo

This demo demonstrates how to use the AutoGen Logger with AutoGen Python SDK to send telemetry data to Azure Monitor.

- cd to `samples/apps/otel-autogen-logger/simple_chat.py`
- Run vscode debugger with the configuration `Python Debugger: Current
- Type a sample message in the in the terminal example "How tall is mt everest?" to trigger the workflow

## AutoGen Insights Workbook

AutoGen insights is streamlined with AgentOps, offering real-time visibility into agent performance and interactions. Easily track metrics such as execution times, costs, and error rates across sessions. The dashboard provides detailed logs and visualizations, helping identify bottlenecks and optimize workflows. This ensures that your AI agents operate efficiently and reliably at scale.

![AutoGen Insights Workbook](./images/autogen_insights.gif)