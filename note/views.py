from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Note
from .forms import NoteForm
from random import choice
# Create your views here.


def create(request):
    
    form = NoteForm(request.POST)
    print(form)
    if form.is_valid():
        new_note = form.save(commit=False)
        form.instance.author = request.user
        print(form.instance.author)
        new_note.save()
        form.save_m2m()
        messages.success(request, 'Note Added Successfully')
        # Redirect Not Happening
        redirect('home')
    context = {
        "form": form
    }
    return render(request, 'note/create-note.html', context)


def show(request, slug):
    note = get_object_or_404(Note, slug=slug)
    
    context = {
        'note': note,
        
    }
    return render(request, 'note/show-note.html', context)


def edit(request, id):
    return render(request, 'note/edit-note.html')


def delete(request, id):
    # Backend Logic here
    get_object_or_404(Note, pk=id).delete()
    return redirect('home')
