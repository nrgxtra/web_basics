from django.shortcuts import render, redirect
from core.get_user_profile import get_profile
from notes.user_notes.models import Note
from notes.user_profile.forms import UserProfileForm


def show_home(request):
    profile = get_profile()
    if not profile:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = UserProfileForm()
            context = {
                'form': form,
            }
            return render(request, 'home-no-profile.html', context)
    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def show_profile(request):
    profile = get_profile()
    notes_count = Note.objects.count()
    if request.method == 'POST':
        profile.delete()
        Note.objects.all().delete()
        return redirect('home')
    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


