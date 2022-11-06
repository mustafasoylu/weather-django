from channel.utils.constants import (
    OPENWEATHER_URL,
    OPENWEATHER_API_KEY,
    OPENWEATHER_DEFAULT_UNIT,
    REQUEST_TIMEOUT,
)
import requests
from .utils.errors import CityNotFoundError, RequestTimeoutError, InvalidAPIKeyError
from .utils.parsers import WeatherResponseMapper
from .utils.validators import validate_language, validate_query, validate_unit


def query_builder(
    query: str, language="", api_key=OPENWEATHER_API_KEY, unit=OPENWEATHER_DEFAULT_UNIT
) -> str:

    validate_query(query)
    validate_unit(unit)

    url = f"{OPENWEATHER_URL}?q={query}&appid={api_key}&units={unit}"
    if language != "":
        validate_language(language)
        url += f"&lang={language}"

    return url


def get_weather(query: str, language="") -> WeatherResponseMapper:
    url = query_builder(query, language)
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            response_json = response.json()

            if response_json["cod"] == 404:
                raise CityNotFoundError(query)
            else:
                return WeatherResponseMapper.from_json(response_json)
        elif response.status_code == 401:
            raise InvalidAPIKeyError(query)
        elif response.status_code == 404:
            raise CityNotFoundError(query)
    except requests.exceptions.Timeout:
        raise RequestTimeoutError(query)
