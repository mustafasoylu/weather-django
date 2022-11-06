from abc import ABC, abstractmethod
from typing import Dict
from channel.models import WeatherResponse


class JsonToObjectMapper(ABC):
    @staticmethod
    @abstractmethod
    def from_json(json_data: Dict):
        pass


class WeatherResponseMapper(JsonToObjectMapper):
    @staticmethod
    def from_json(json_data: dict) -> WeatherResponse:
        try:
            icon = json_data["weather"][0]["icon"]
            description = json_data["weather"][0]["description"]
            longitude = json_data["coord"]["lon"]
            latitude = json_data["coord"]["lat"]
            temperature = json_data["main"]["temp"]
            temperature_min = json_data["main"]["temp_min"]
            temperature_max = json_data["main"]["temp_max"]
            pressure = json_data["main"]["pressure"]
            humidity = json_data["main"]["humidity"]
            name = json_data["name"]
            wind_speed = json_data["wind"]["speed"]
            wind_angle = json_data["wind"]["deg"]

            return WeatherResponse(
                icon=icon,
                name=name,
                description=description,
                longitude=longitude,
                latitude=latitude,
                temperature=temperature,
                temperature_min=temperature_min,
                temperature_max=temperature_max,
                pressure=pressure,
                humidity=humidity,
                wind_speed=wind_speed,
                wind_angle=wind_angle,
            )

        except KeyError:
            raise Exception("Error parsing while parsing the weather response.")
