from django.shortcuts import render, redirect

from expenseTracker.core.profile_utils import get_profile
from expenseTracker.expenses.forms import ExpenseForm, DeleteExpenseForm
from expenseTracker.expenses.models import Expense


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('profile create')
    expenses = Expense.objects.all()
    budget = profile.budget
    budget_left = budget - sum(e.price for e in expenses)
    context = {
        'expenses': expenses,
        'budget': budget,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        context = {
            'form': form,
            'expense': expense
        }
        return render(request, 'expense-edit.html', context)
    form = ExpenseForm(request.POST, instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('home')
    else:
        form = DeleteExpenseForm(instance=expense)
        context = {
            'form': form,
            'expense': expense,
        }
        return render(request, 'expense-delete.html', context)


