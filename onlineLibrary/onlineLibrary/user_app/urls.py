from django.urls import path

from onlineLibrary.user_app.views import show_home, create_profile, show_profile, edit_profile, delete_profile

urlpatterns = [
    path('', show_home, name='home'),
    path('create_user', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]

