from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


# Login view (Django built-in)
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# Logout view (Django built-in)
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
