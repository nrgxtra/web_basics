from django.urls import path

from onlineLibrary.books_app.views import add_book, edit_book, book_details, book_delete

urlpatterns = [
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', book_details, name='book details'),
    path('delete/<int:pk>', book_delete, name='book delete'),
]
