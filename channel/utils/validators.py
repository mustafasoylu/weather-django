from .constants import OPENWEATHER_UNITS, OPENWEATHER_LANGUAGES
from .errors import InternalAPIQueryError


def validate_query(query: str):
    if not query or query == "":
        raise InternalAPIQueryError("query is null or empty")


def validate_unit(unit: str):
    if unit not in OPENWEATHER_UNITS:
        raise InternalAPIQueryError(f"Wrong unit of measurement: {unit}")


def validate_language(language: str):
    if language not in OPENWEATHER_LANGUAGES:
        raise InternalAPIQueryError(
            f"Only {', '.join(OPENWEATHER_LANGUAGES)} is allowed as language."
        )
