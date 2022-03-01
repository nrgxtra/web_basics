from django.urls import path

from todos.todos_app.views import show_todos, update_todo, delete_todo, create_todo

urlpatterns = [
    path('', show_todos, name='index'),
    path('update/<int:pk>', update_todo, name='update'),
    path('delete/<int:pk>', delete_todo, name='delete'),
    path('create/', create_todo, name='create'),
]