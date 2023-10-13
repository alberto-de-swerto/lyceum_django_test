from django.test import TestCase, Client
from random import randint


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_endpoint(self):
        response = Client().get('catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_int_endpoint(self):
        response = Client().get(f'catalog/{randint(1, 100)}/')
        self.assertEqual(response.status_code, 200)

    def test_about_endpoint(self):
        response = Client().get('about/')
        self.assertEqual(response.status_code, 200)
