from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegistrationForm


def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                req, f'ACCESS ISSUED: User {username} granted Level 1 access.')        
            return redirect('books:index')
    else:
        form = UserRegistrationForm()
    
    return render(req, 'users/register.html', {'form': form})
