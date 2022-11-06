from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from .controllers import get_weather
from .utils.errors import (
    CityNotFoundError,
    RequestTimeoutError,
    ResponseParsingError,
    InvalidAPIKeyError,
    InternalAPIQueryError,
)
from .utils.constants import PAGE_TEXTS, PAGE_CACHING_LIMIT
import json


@cache_page(PAGE_CACHING_LIMIT)
def index(request):
    texts = json.dumps(PAGE_TEXTS)
    if request.method == "POST":
        city = request.POST["city"]
        language = request.POST["language"]

        template = loader.get_template("index.html")
        context = {"city": city.capitalize(), "language": language, "texts": texts}

        try:
            weather = get_weather(city.lower(), language.lower())
            context["response"] = weather
            return HttpResponse(template.render(context, request))
        except (
            CityNotFoundError,
            RequestTimeoutError,
            ResponseParsingError,
            InvalidAPIKeyError,
            InternalAPIQueryError,
        ) as e:
            context["error_message"] = e.message
            return HttpResponse(template.render(context, request))
        except:
            context["error_message"] = "Unknown error. Please contact your admin."
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("index.html")
        return HttpResponse(
            template.render({"texts": texts, "language": "en"}, request)
        )
