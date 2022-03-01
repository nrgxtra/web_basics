from django.shortcuts import render, redirect

from Recipes.recipe_app.forms import CreateRecipeForm, DeleteRecipeForm
from Recipes.recipe_app.models import Recipe


def show_home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)
    context = {
        'form': CreateRecipeForm(),
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = CreateRecipeForm(instance=recipe)
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)
    context = {
        'form': form,
    }
    return render(request, 'edit.html', context)


def show_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = []
    current = ''
    for item in recipe.ingredients:
        if item != ' ' and item != ',':
            current += item
        elif item == ' ':
            pass
        else:
            ingredients.append(current)
            current = ''
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    form = DeleteRecipeForm(instance=recipe)
    context = {
        'form': form,
    }
    return render(request, 'delete.html', context)
