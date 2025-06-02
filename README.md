# weather_agent_mcp

## General Service Description
This client provides an interface for interacting with the MCP server, which offers an API to fetch the current weather for a specified city. The client uses Gradio to create a user-friendly interface and interacts with the MCP server to obtain weather data.

### Resource
* Ubuntu 24.04.1
* NGC Cli
* Docker 27.3.1
* nvidia-container-toolkit
* cuda-toolkit 12.6
* open-driver 560
* HDD 160Gb
* RTX2080TI

## Technology Stack
- Python
- FastAPI
- FastMCP
- Gradio
- OpenWeatherMap API
- Docker-Compose
- Ollama

## Functional Requirements
- Fetch weather data for a specified city.
- Display weather description and temperature in Celsius.
- Handle errors for incorrectly specified cities.
- Interactive interface for entering a city and obtaining weather data.


## Deployment using Docker Compose

To deploy the project locally, use Docker Compose. Ensure you have Docker and Docker Compose installed.

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the command:

```bash
sudo sh configure_VM.sh
```

This will deploy three services: `mcp_server`, `mcp_client_gradio`, and `ollama`.

## License
This project is licensed under the terms of the MIT License.