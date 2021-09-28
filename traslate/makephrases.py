from reddis import WriteDictionary
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
WriteDictionary(r, "Welcome to my site", {"ru": "Добро пожаловать на мой сайт", "en": "Welcome to my site", "de": "Willkommen auf meiner Seite"})