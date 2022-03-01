from django.shortcuts import render, redirect

from notes.user_notes.forms import CreateNoteForm, DeleteNoteForm
from notes.user_notes.models import Note


def create_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form,
        }
        return render(request, 'note-create.html', context)
    form = CreateNoteForm()
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

        form = CreateNoteForm(instance=note)
        context = {
            'form': form,
            'note': note,
        }
        return render(request, 'note-edit.html', context)
    else:
        form = CreateNoteForm(instance=note)
        context = {
            'form': form,
            'note': note,
        }
        return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)
