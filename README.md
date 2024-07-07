# Weather-app
The final project of CS50 Python

#### Description:
This Weather App is a Python-based application that allows users to check current weather conditions and 5-day forecasts for cities around the world. The app utilizes the OpenWeatherMap API to fetch real-time weather data.

### Features:
- Current weather display: Shows temperature, humidity, wind speed, and weather description
- 5-day forecast: Provides a daily forecast at noon for the next 5 days

### Files:
- `project.py`: The main Python script containing the WeatherApp class and core functionality
  - `WeatherApp`
  - `get_current_weather()`: Fetches current weather data from the API
  - `get_forecast()`: Retrieves 5-day forecast data
  - `main()`: Initializes and runs the application

- `test_project.py`: Contains pytest functions to test the core weather data retrieval functions
  - `test_get_current_weather()`: Ensures current weather data is correctly fetched
  - `test_get_forecast()`: Verifies forecast data retrieval
  - `test_invalid_city_current_weather()`: Tests error handling for invalid city names
  - `test_invalid_city_forecast()`: Checks forecast error handling for invalid inputs

- `requirements.txt`: Lists the required Python packages (requests and pytest)

### Design Choices:


1. API Selection: OpenWeatherMap was selected for its reliable and free tier service, providing both current weather and forecast data.

2. Error Handling: The app includes error messages for invalid city names or API issues, enhancing user experience.

### How to Run:
1. Ensure Python is installed on your system
2. Install required packages: `pip install -r requirements.txt`
3. Replace "your_api_key_here" in `project.py` with your OpenWeatherMap API key
4. Run the app: `python project.py`
5. To run tests: `pytest test_project.py`

This Weather App project demonstrates proficiency in Python programming, API integration, and software testing practices.
