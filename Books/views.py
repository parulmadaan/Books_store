from django.shortcuts import render, redirect
from django.http import HttpResponse
from Books.forms import createbookform
from .models import Books
from Author.models import User
from Author import views
# from .forms import *
# Create your views here.


def add_book(request):
    if request.method == 'POST':
        auth = request.POST.get('username')
        title = request.POST.get('title')
        Price = request.POST.get('Price')
        Edition = request.POST.get('Edition')
        users = User.objects.get(email=auth)
        books_data = Books(author=users, title=title,
                           Price=Price, Edition=Edition)
        books_data.save()
        data = Books.objects.filter(author_id=request.user.id)
        return render(request, 'books/viewbooks.html', {"data": data})
        # return render(request,'books/viewbooks.html')

    return render(request, 'books/addbook.html')


def view_books(request):
    data = Books.objects.filter(author_id=request.user.id)
    return render(request, 'books/viewbooks.html')
