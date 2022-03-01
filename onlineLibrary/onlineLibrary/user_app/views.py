from django.shortcuts import render, redirect

from onlineLibrary.books_app.models import Book
from onlineLibrary.user_app.forms import UserForm, DeleteUser
from onlineLibrary.user_app.models import Profile


def show_home(request):
    user = Profile.objects.first()
    if not user:
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)
    books = Book.objects.all()
    context = {
        'user': user,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    user = Profile.objects.first()
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    user = Profile.objects.first()
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'edit-profile.html', context)
    form = UserForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    user = Profile.objects.first()
    books = Book.objects.all()
    if request.method == 'POST':
        Profile.objects.all().delete()
        books.delete()
        return redirect('home')

    if request.method == 'GET':
        form = DeleteUser(instance=user)
        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'delete-profile.html', context)


