
import requests

def get_weather():
    city = input("Enter the name of the city: ")
    api_key = "7f6aa5bfaa2dc7705abbf43f73751af7"  # Replace with your actual API key (now in quotes)
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    # Make the request
    response = requests.get(base_url, params=params)

    # Debug: Print the raw response for troubleshooting
    print(f"Debug Info: {response.status_code}, {response.text}")

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error: Could not fetch weather data. Status code: {response.status_code}")
        print("Please check the city name, API key, or try again later.")

if __name__ == "__main__":
    get_weather()