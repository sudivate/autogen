# AutoGen Observabily with OpenTelemetry

This is a example of how to use the OpenTelemetry SDK to instrument Autogen application and send telemetry data to Azure Monitor.


## Instrumentation implemented in this example

| Instrumentation | Description |
|-----------------|-------------|
| [OTel Logger](./../../../autogen/logger/otel_logger.py) | Added new logger to core Autogen SDK. This will enable `autogen.runtime_logging.start(logger_type="otel", config={})`(TODO: Create UpStream PR)   |
| [OTel Logger by Overriding Base Logger](./otel_logger.py) | Overriding Baselogger by implementing BaseLogger abstraction. This can be used without the upstream changes to AutoGen SDK |

## Demo Prerequisites
- Clone the repository(https://github.com/sudivate/autogen/tree/sudivate/otel-playground)
- Open the project in Visual Studio Code and reopen the project in the devcontainer(studio) VS code will prompt you to do this
- Rename the `env.example` file to `.env` and update the values for AZURE_APPINSIGHTS_CONNECTION_STRING and AZURE_OPENAI_API_KEY
- Install required dependencies by running `pip install -r ./samples/apps/otel-autogen-logger/requirements.txt`
- Add debug configuration in the `.vscode/launch.json` file
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


## AutoGen Studio Demo
- Run vscode debugger with the configuration `Python Debugger: FastAPI`
- Open the browser and navigate to `http://localhost:8081/` You should see the Autogen Studio UI
- Configure the Travel planning Workflow with Azure Open AI and run the workflow in new session

## AutoGen Logger Demo
- cd to `samples/apps/otel-autogen-logger/simple_chat.py`
- Run vscode debugger with the configuration `Python Debugger: Current


## Autogen Insights workbook

Sample workbook to visualize the telemetry data in Azure Monitor

![Autogen Insights Workbook](./images/autogen-insights.png)