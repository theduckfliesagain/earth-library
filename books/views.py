from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book

def index(req):
    data = Book.objects.all()
    return render(req, 'books/index.html', {'books':data})

@login_required
def show(req, book_id):
    data = get_object_or_404(Book, pk=book_id)
    print(data)
    return render(req, 'books/show.html', {'book':data})
