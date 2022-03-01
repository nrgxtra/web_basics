from django.shortcuts import render, redirect

# Create your views here.
from book.book_app.forms import BookForm
from book.book_app.models import Book


def show_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def show_create_form(request, form):
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def show_update_form(request, form):
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def create_book(request):
    if request.method == 'GET':
        context = {
            'form': BookForm
        }
        return render(request, 'create.html', context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_create_form(request, form)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': BookForm(initial=book.__dict__)
        }
        return render(request, 'edit.html', context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_update_form(request, form)
