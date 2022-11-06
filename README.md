# wheather-django

Coding challenge for CheMondis.

## Description for example code

The user can enter the name of city he would like to know the current weather at. The result should contain information on:

-   the requested city
-   temperature, min. temperature, max. temperature
-   humidity, pressure
-   wind speed and direction **(an arrow showing the exact angle)**
-   description
-   BONUS: location of the input city on map using leaflet.

Also below values are set in channel/utils/constants.py and can be changed.

The data is shown in the metric unit system.

```python
OPENWEATHER_DEFAULT_UNIT = "metric"
```

The results are cached for a configurable amount of time (5, 10, 60 minutes).

```python
PAGE_CACHE_MINUTES = 5
```

The application supports English, Japanese and Turkish. A new language can be added too, but proper translation for showing the front end texts have to be added to PAGE_TEXTS as a variable.

```python
OPENWEATHER_LANGUAGES = ["tr", "en", "ja"]
PAGE_TEXTS = {
    "en": {...},
    "tr": {...},
    "ja": {...},
}
```

Finally, the weather data is retrieved through [OpenWeather](https://openweathermap.org/) usign the below API key. **Please enter your API Key before running any test or the application itself.**

## Implementation

Above project is implemented using django. Unit tests are written using unittest library. **Please enter your API Key before running any test or the application itself.**

### Setup

In order to do tests or to run the applicatio on your local environment, python libraries must be installed. The setup can be done easily by below script.

```bash
./scripts/setup.sh
```

### Testing

Run below command to do all unit tests.

```bash
./scripts/run_tests.sh
```

## How to run

Scripts for development and production is explained below. All code is only tested on MacOS Ventura 13.0 with Intel chip.

### Development Environment

Django runs in debug mode in development script. You can access your application on port [8000](http://127.0.0.1:8000/).

```bash
./scripts/run_dev.sh
```

### Production Environment

Django runs in production mode with uwsgi and nginx in production environment. You can directly access to the application by directly [localhost](http://127.0.0.1/).

```bash
./scripts/run_prod.sh
```

## License

Copyright (c) 2022 Mustafa Soylu

This software is released under the MIT License, see LICENSE.
