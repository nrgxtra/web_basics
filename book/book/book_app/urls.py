from django.urls import path

from book.book_app.views import show_books, create_book, edit_book

urlpatterns = [
    path('', show_books, name='index'),
    path('create/', create_book, name='create'),
    path('edit/<int:pk>', edit_book, name='edit'),
]