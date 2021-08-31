from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('addbook/',views.add_book,name='addbook'),
    path('viewbooks/',views.view_books,name='viewbooks'),
]
