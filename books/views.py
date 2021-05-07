from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
# Create your views here.
books_data = [
    {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency',
        'author': 'Alexander McCall Smith'}
]


def index(req):
    data = Book.objects.all()
    return render(req, 'books/index.html', {'books':data})

def show(req, book_id):
    data = get_object_or_404(Book, pk=book_id)
    print(data)
    return render(req, 'books/show.html', {'book':data})
