from django import forms

from onlineLibrary.books_app.models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
