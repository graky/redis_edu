from django.test import TestCase
from django.urls import reverse


class TestLanguage(TestCase):

    def test_russian(self):
        headers = {"HTTP_ACCEPT_LANGUAGE": "ru"}
        url = reverse("welcome")
        response = self.client.get(url, **headers)
        result = response.content.decode("utf-8")
        self.assertEqual(result, "Добро пожаловать на мой сайт")

    def test_default(self):
        url = reverse("welcome")
        response = self.client.get(url)
        result = response.content.decode("utf-8")
        self.assertEqual(result, "Welcome to my site")

    def test_english(self):
        headers = {"HTTP_ACCEPT_LANGUAGE": "en"}
        url = reverse("welcome")
        response = self.client.get(url, **headers)
        result = response.content.decode("utf-8")
        self.assertEqual(result, "Welcome to my site")
