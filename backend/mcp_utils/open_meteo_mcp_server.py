import httpx
from mcp.server import FastMCP

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    #Düsseldorf
	"latitude": 51.2217,
	"longitude": 6.7762,
	"daily": ["temperature_2m_max", "temperature_2m_min", "rain_sum", "snowfall_sum", "wind_speed_10m_max"],
	"hourly": ["temperature_2m", "rain", "showers", "wind_speed_10m"],
	"models": "icon_seamless",
	"timezone": "Europe/Berlin",
}

weather_mcp = FastMCP("weather")

def getWeather():
    response = httpx.get(URL, params=params)
    return response.text

#TODO: tool bennen
@weather_mcp.tool()
def getWeatherTool():
    return getWeather()

def main():
    weather_mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()