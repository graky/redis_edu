from django.http import HttpResponse
from django.utils.translation import get_language_from_request
from .reddis import GetDictionary
import redis
from django.conf import settings

r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def welcome_view(request):
    output = "Welcome to my site"
    lang = get_language_from_request(request, check_path=True)
    output = GetDictionary.get_dictionary(r, output, lang=lang)
    return HttpResponse(output)


def your_lang(request):
    output = "It's seems like your language is "
    lang = get_language_from_request(request, check_path=True)
    output = GetDictionary.get_dictionary(r, output, lang=lang)
    output += lang
    return HttpResponse(output)
