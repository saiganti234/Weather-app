import pytest
from project import get_current_weather, get_forecast, display_weather

def test_get_current_weather():
    weather_data = get_current_weather("London")
    assert weather_data["cod"] == 200
    assert "main" in weather_data
    assert "temp" in weather_data["main"]

def test_get_forecast():
    forecast_data = get_forecast("New York")
    assert forecast_data["cod"] == "200"
    assert "list" in forecast_data
    assert len(forecast_data["list"]) > 0

def test_display_weather(capsys):
    mock_data = {
        "cod": 200,
        "name": "Test City",
        "main": {"temp": 20, "humidity": 50},
        "wind": {"speed": 5},
        "weather": [{"description": "clear sky"}]
    }
    display_weather(mock_data)
    captured = capsys.readouterr()
    assert "Test City" in captured.out
    assert "Temperature: 20°C" in captured.out
    assert "Humidity: 50%" in captured.out
    assert "Wind Speed: 5 m/s" in captured.out
    assert "Description: clear sky" in captured.out
