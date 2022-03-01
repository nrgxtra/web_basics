from django.urls import path

from notes.user_profile.views import show_home, show_profile

urlpatterns = [
    path('', show_home, name='home'),
    path('profile/', show_profile, name='profile'),
]
