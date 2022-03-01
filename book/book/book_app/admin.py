from django.contrib import admin

# Register your models here.
from book.book_app.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pages', 'description', 'author']


admin.site.register(Book, BookAdmin)

