from reddis import WriteDictionary
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
WriteDictionary(r, "Welcome to my site", {"ru": "Добро пожаловать на мой сайт", "en": "Welcome to my site", "de": "Willkommen auf meiner Seite"})
WriteDictionary(r, "It's seems like your language is ", {"ru": "Похоже твой язык это ", "en": "Welcome to my site", "de": "Anscheinend ist deine Sprache "})