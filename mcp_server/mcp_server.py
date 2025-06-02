from fastmcp import FastMCP
import requests

# Create an MCP server
mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': "d852c26a2ec8983bf0b3932f78dff564",
        'units': 'metric'  # Используем метрическую систему для температуры в градусах Цельсия
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"weather in {location}: {weather}. Temperature: {temperature}°C."
    else:
        return "Не удалось получить данные о погоде. Пожалуйста, проверьте название города и попробуйте снова."


# Run the server
mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=8000,
        log_level="debug"
    )
