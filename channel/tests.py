from django.test import TestCase
from unittest.mock import MagicMock, patch

from .controllers import query_builder, get_weather
from .utils.validators import validate_language, validate_query, validate_unit
from .utils.constants import OPENWEATHER_URL, REQUEST_TIMEOUT
from .utils.errors import InternalAPIQueryError


class ControllerTests(TestCase):
    API_KEY = "key"
    QUERY = "sendai"
    LANGUAGE = "tr"
    UNIT = "metric"
    EXPECTED_URL = (
        f"{OPENWEATHER_URL}?q={QUERY}&appid={API_KEY}&units={UNIT}&lang={LANGUAGE}"
    )

    def test_query_builder(self):
        url = query_builder(self.QUERY, self.LANGUAGE, self.API_KEY, self.UNIT)

        self.assertEqual(
            url,
            self.EXPECTED_URL,
            f"query_builder failed. Expected {self.EXPECTED_URL}, but got {url}",
        )

    @patch("channel.controllers.requests")
    def test_get_weather(self, mocked):
        mocked.get = MagicMock()
        expected_url = query_builder(self.QUERY, self.LANGUAGE)
        get_weather(self.QUERY, self.LANGUAGE)

        mocked.get.assert_called_once_with(expected_url, timeout=REQUEST_TIMEOUT)


class ValidatorsTests(TestCase):
    INVALID_QUERY = ""
    VALID_QUERY = "sendai"
    INVALID_UNIT = "test_unit"
    VALID_UNIT = "imperial"
    INVALID_LANGUAGE = "fr"
    VALID_LANGUAGE = "ja"

    def test_validate_query(self):
        try:
            validate_query(self.VALID_QUERY)
        except InternalAPIQueryError:
            self.fail("validate_query() raised InternalAPIQueryError unexpectedly!")

        with self.assertRaises(InternalAPIQueryError):
            validate_query(self.INVALID_QUERY)

    def test_validate_unit(self):
        try:
            validate_unit(self.VALID_UNIT)
        except InternalAPIQueryError:
            self.fail("validate_unit() raised InternalAPIQueryError unexpectedly!")

        with self.assertRaises(InternalAPIQueryError):
            validate_unit(self.INVALID_UNIT)

    def test_validate_language(self):
        try:
            validate_language(self.VALID_LANGUAGE)
        except InternalAPIQueryError:
            self.fail("validate_language() raised InternalAPIQueryError unexpectedly!")

        with self.assertRaises(InternalAPIQueryError):
            validate_language(self.INVALID_LANGUAGE)
