from django.contrib import admin

from petstagram2.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'age']

# admin.site.register(Pet, PetAdmin)
