from django.urls import path

from expenseTracker.profiles.views import edit_profile, delete_profile, profile_details, create_profile

urlpatterns = [
    path('', profile_details, name='profile page'),
    path('create/', create_profile, name='profile create'),
    path('edit/', edit_profile, name='profile edit'),
    path('delete/', delete_profile, name='profile delete'),
]
