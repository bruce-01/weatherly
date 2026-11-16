
import requests


# 1. Convert city name into geographical coordinates

def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "country": location.get("country", ""),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


# 2. Fetch current weather and 7-day forecast

def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "is_day",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
            "wind_direction_10m"
        ],

        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "sunrise",
            "sunset",
            "precipitation_probability_max"
        ],

        "timezone": "auto",
        "forecast_days": 7
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


# 3. Convert weather codes into readable descriptions

def get_weather_description(code):

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    return weather_codes.get(code, "Unknown weather")


# 4. Convert weather codes into icons

def get_weather_icon(code):

    if code == 0:
        return "☀️"

    elif code in [1, 2]:
        return "⛅"

    elif code == 3:
        return "☁️"

    elif code in [45, 48]:
        return "🌫️"

    elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
        return "🌧️"

    elif code in [71, 73, 75]:
        return "❄️"

    elif code in [95, 96, 99]:
        return "⛈️"

    return "🌡️"
