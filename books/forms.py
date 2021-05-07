from django import forms
from django.forms import widgets
from .models import Book

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author")
        widgets = {"borrower" : forms.HiddenInput()}

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("borrower",)
        widgets = {"borrower" : forms.HiddenInput()}


    
