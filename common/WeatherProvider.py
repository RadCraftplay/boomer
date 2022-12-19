
import re
from typing import Callable

import requests


class WeatherProvider():
    def __init__(self, api_settings) -> None:
        self.__api_key : str = api_settings["openweatherapi_key"]
    
    def get_current_weather_from_match(self, match: re.Match) -> Callable[[], str]:
        city_name = match.group(1)
        return self.get_current_weather_in_city(city_name)
    
    def get_current_weather_in_city(self, city_name: str) -> Callable[[], str]:
        base_current_weather_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_current_weather_url + "appid=" + self.__api_key + "&units=metric&q=" + str(city_name)
        response = requests.get(complete_url)
        resp_json = response.json()

        if resp_json["cod"] == "404":
            return lambda: "City not found!"

        main_weather_data = resp_json["main"]
        current_temperature = int(main_weather_data["temp"])
        feels_like_temperature = int(main_weather_data["feels_like"])
        current_pressure = main_weather_data["pressure"]
        current_humidity = main_weather_data["humidity"]
        additional_weather_info = resp_json["weather"]
        weather_description = additional_weather_info[0]["description"]

        return lambda: str.format("Currently in {} the weather is: {}. The temperature is {} Celsius (feels like {} Celsius). The atmospheric pressure is {}hPa, and the humidity is {}%.",
            city_name, weather_description, current_temperature, feels_like_temperature, current_pressure, current_humidity)