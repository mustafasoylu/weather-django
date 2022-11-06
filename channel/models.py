from dataclasses import dataclass
from django.db import models


@dataclass
class WeatherResponse:
    icon: str
    name: str
    description: str
    longitude: str
    latitude: str
    temperature: float
    temperature_min: float
    temperature_max: float
    pressure: int
    humidity: int
    wind_speed: float
    wind_angle: float
