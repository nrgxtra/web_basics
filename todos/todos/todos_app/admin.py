from django.contrib import admin

# Register your models here.
from todos.todos_app.models import Todo, Person, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_done', 'person_responsible',]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)