from django.urls import path

from notes.user_notes.views import create_note, edit_note, delete_note, note_details

urlpatterns = [
    path('add/', create_note, name='note create'),
    path('edit/<int:pk>', edit_note, name='note edit'),
    path('delete/<int:pk>', delete_note, name='note delete'),
    path('details/<int:pk>', note_details, name='note details'),
]
