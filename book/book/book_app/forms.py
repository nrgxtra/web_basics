from django import forms

from book.book_app.models import Book


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class BookForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Book
        fields = '__all__'

