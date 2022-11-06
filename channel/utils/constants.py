OPENWEATHER_API_KEY = ""
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_UNITS = ["standard", "metric", "imperial"]
OPENWEATHER_LANGUAGES = ["tr", "en", "ja"]
OPENWEATHER_DEFAULT_UNIT = "metric"
REQUEST_TIMEOUT = 2
PAGE_CACHE_MINUTES = 5
PAGE_CACHING_LIMIT = 60 * PAGE_CACHE_MINUTES

PAGE_TEXTS = {
    "en": {
        "button": "Get",
        "wind": "Wind",
        "humidity": "Humidity",
        "pressure": "Pressure",
        "weather": "Weather",
        "placeholder": "City name",
    },
    "tr": {
        "button": "Getir",
        "wind": "Rüzgar",
        "humidity": "Nem",
        "pressure": "Basınç",
        "weather": "Hava Durumu",
        "placeholder": "Şehir İsmi",
    },
    "ja": {
        "button": "取得",
        "wind": "風",
        "humidity": "湿度",
        "pressure": "空気圧",
        "weather": "天気予報",
        "placeholder": "都市名",
    },
}
