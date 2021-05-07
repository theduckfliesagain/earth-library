from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import NewBookForm, BorrowBookForm


def index(req):
    data = Book.objects.all()
    return render(req, 'books/index.html', {'books': data})


@login_required
def show(req, book_id):
    data = get_object_or_404(Book, pk=book_id)
    print(data)
    return render(req, 'books/show.html', {'book': data})


@login_required
def new(req):
    if req.method == 'POST':
        form = NewBookForm(req.POST)
        if form.is_valid():
            new_book_id = form.save().id
            # messages.success(
            #     req, f'ACCESS ISSUED: User {username} granted Level 1 access.')
            return redirect('books:show', book_id= new_book_id)
    else:
        form = NewBookForm()
        
    return render(req, 'books/new.html', {'form': form})
