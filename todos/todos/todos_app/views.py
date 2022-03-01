from django.shortcuts import render, redirect

# Create your views here.
from todos.todos_app.forms import TodoForm
from todos.todos_app.models import Todo


def show_todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def create_todo(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'GET':
        form = TodoForm(initial=todo.__dict__)
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('index')

