from django.urls import path

from Recipes.recipe_app.views import show_home, create_recipe, edit_recipe, show_recipe, delete_recipe

urlpatterns = [
    path('', show_home, name='home'),
    path('create/', create_recipe, name='create'),
    path('edit/<int:pk>', edit_recipe, name='edit'),
    path('details/<int:pk>', show_recipe, name='details'),
    path('delete/<int:pk>', delete_recipe, name='delete'),
]

