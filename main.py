from weather.weather_services import get_weather
import os
from dotenv import load_dotenv

def main():
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("❌ API key not found. Please check your .env file.")
        return

    city = input("Enter city name: ")
    weather = get_weather(city, api_key)

    if "error" in weather:
        print("Error:", weather["error"])
    else:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Icon code: {weather['icon']}")

if __name__ == "__main__":
    main()
