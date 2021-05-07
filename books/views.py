from django.http import request
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
    book = get_object_or_404(Book, pk=book_id)
    if req.method == 'POST':
        form = BorrowBookForm(req.POST)

        if form.is_valid():
            if(book.borrower == req.user):
                book.borrower = None
                msg = f"ACCESS REVOKED: Returned '{book.title}'."
            else:
                book.borrower = req.user
                msg = f"ACCESS ISSUED: Borrowed '{book.title}'."

            book.save()
            messages.success(req, f"ACCESS ISSUED: Borrowed '{book.title}'.")
            return redirect('books:show', book_id= book_id)
    else:
        form = BorrowBookForm(initial={'borrower': req.user})

    return render(req, 'books/show.html', {'book': book, 'form': form})


@login_required
def new(req):
    print(req)
    if req.method == 'POST':
        form = NewBookForm(req.POST)
        if form.is_valid():
            new_book_id = form.save().id
            # messages.success(
            #     req, f'ACCESS ISSUED: User {username} granted Level 1 access.')
            return redirect('books:show', book_id=new_book_id)
    else:
        form = NewBookForm()

    return render(req, 'books/new.html', {'form': form})
