class CityNotFoundError(Exception):
    """Exception raised for errors in OpenWeather API calls.

    Attributes:
        query -- input query to find the weather
        message -- explanation of the error
    """

    def __init__(self, query, message="City not found"):
        self.query = query
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.query} -> {self.message}"


class RequestTimeoutError(Exception):
    """Exception raised for timeout errors in OpenWeather API calls.

    Attributes:
        query -- input query to find the weather
        message -- explanation of the error
    """

    def __init__(
        self,
        query,
        message="Request timed out. Please wait a little before another request.",
    ):
        self.query = query
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.query} -> {self.message}"


class ResponseParsingError(Exception):
    """Exception raised for parsing in OpenWeather API responses.

    Attributes:
        query -- input query to find the weather
        message -- explanation of the error
    """

    def __init__(
        self,
        query,
        message="API response is not expected. Please contact your admin.",
    ):
        self.query = query
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.query} -> {self.message}"


class InvalidAPIKeyError(Exception):
    """Exception raised if OpenWeather API Key is not valid.

    Attributes:
        query -- input query to find the weather
        message -- explanation of the error
    """

    def __init__(
        self,
        query,
        message="Your OpenWeather API Key is invalid. Please contact your admin.",
    ):
        self.query = query
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.query} -> {self.message}"


class InternalAPIQueryError(Exception):
    """Exception raised if OpenWeather API query is invalid.

    Attributes:
        query -- input query to find the weather
        message -- explanation of the error
    """

    def __init__(
        self,
        query,
        message="Internal Error. OpenWeather API query is invalid. Please contact your admin.",
    ):
        self.query = query
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.query} -> {self.message}"
