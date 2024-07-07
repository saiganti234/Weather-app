import requests
import json
from datetime import datetime

API_KEY = "33b09295cf47869971d13ce3adcfe14f"

def main():
    while True:
        print("\nWeather App")
        print("1. Get current weather")
        print("2. Get 5-day forecast")
        print("3. Manage favorite cities")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            city = input("Enter city name: ")
            weather_data = get_current_weather(city)
            display_weather(weather_data)
        elif choice == '2':
            city = input("Enter city name: ")
            forecast_data = get_forecast(city)
            display_forecast(forecast_data)
        elif choice == '3':
            manage_favorites()
        elif choice == '4':
            print("Thank you for using the Weather App!")
            break
        else:
            print("Invalid choice. Please try again.")

def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return json.loads(response.text)

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return json.loads(response.text)

def display_weather(weather_data):
    if weather_data["cod"] != 200:
        print(f"Error: {weather_data['message']}")
        return

    print(f"\nCurrent weather in {weather_data['name']}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    print(f"Description: {weather_data['weather'][0]['description']}")

def display_forecast(forecast_data):
    if forecast_data["cod"] != "200":
        print(f"Error: {forecast_data['message']}")
        return

    print(f"\n5-day forecast for {forecast_data['city']['name']}:")
    for item in forecast_data['list']:
        date = datetime.fromtimestamp(item['dt'])
        if date.hour == 12:  # Display forecast for noon each day
            print(f"{date.strftime('%Y-%m-%d')}:")
            print(f"  Temperature: {item['main']['temp']}°C")
            print(f"  Description: {item['weather'][0]['description']}")

def manage_favorites():
    # This function can be implemented to add/remove favorite cities
    # For simplicity, we'll just print a placeholder message
    print("Favorite cities management - To be implemented")

if __name__ == "__main__":
    main()
