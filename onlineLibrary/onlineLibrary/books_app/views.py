from django.shortcuts import render, redirect

from onlineLibrary.books_app.forms import CreateBookForm
from onlineLibrary.books_app.models import Book
from onlineLibrary.user_app.models import Profile


def add_book(request):
    user = Profile.objects.first()
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'add-book.html', context)
    form = CreateBookForm()
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    user = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form,
            'user': user,
            'book': book,
        }
        return render(request, 'edit-book.html', context)
    form = CreateBookForm(instance=book)
    context = {
        'form': form,
        'user': user,
        'book': book,
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    user = Profile.objects.first()
    context = {
        'book': book,
        'user': user,
    }
    return render(request, 'book-details.html', context)


def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')

