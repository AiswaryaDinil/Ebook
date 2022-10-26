from django.test import TestCase
from rest_framework.test import APITestCase
from bookapi.models import Books
from rest_framework.reverse import reverse
from rest_framework import status


class BookTestCase(APITestCase):
    def test_book(self):
        book_data = {
            'title': 'aiswarya',
            'author': 'dinil',
            'genre': 'mystery',
            'favourite': False
        }
        book_obj = Books.objects.create(**book_data)
        # print(f"book_obj{book_obj}")
        url = reverse('book')
        response = self.client.post(url, {'pk': book_obj.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
