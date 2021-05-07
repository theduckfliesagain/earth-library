from django.http import response
from django.test import  Client, TestCase
from django.urls import reverse

from .models import Book, Author

class BaseTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.author = Author.objects.create(name='Test Author')
        cls.book = Book.objects.create(title='Test Book', author= cls.author)

class TestBasicViews(BaseTestCase):
    c = Client()

    def test_index(self):
        response = self.c.get(reverse('books:index'))
        assert 'books' in response.context
        assert response.context['books'].count() == 1
        assert 'books/index.html' in [t.name for t in response.templates]

    def test_show(self):
        response = self.c.get(reverse(('books:show'), kwargs={'book_id': self.book.id}))
        assert 'book' in response.context
        assert response.context['book'].title == 'Test Book'
        assert 'books/show.html' in [t.name for t in response.templates]
