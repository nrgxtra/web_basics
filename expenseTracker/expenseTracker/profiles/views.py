from django.shortcuts import render, redirect

from expenseTracker.core.profile_utils import get_profile
from expenseTracker.expenses.models import Expense
from expenseTracker.profiles.forms import ProfileForm


def profile_details(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(ex.price for ex in expenses)
    context = {
        'profile': profile,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    if request.method == 'POST':
        expenses.delete()
        profile.delete()
        return redirect('home')
    else:
        context = {
            'profile': profile,
        }
        return render(request, 'profile-delete.html', context)

