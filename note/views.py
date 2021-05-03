from django.shortcuts import render,get_object_or_404,redirect
from .models import Note
from .forms import NoteForm
# Create your views here.

def create(request):
    form  = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.save()
        form.save_m2m()
    context = {
        "form":form
    }
    return render(request,'note/create-note.html',context)

def show(request,id):
    return render(request,'note/show-note.html')


def edit(request,id):
    return render(request,'note/edit-note.html')


def delete(request,id):
    # Backend Logic here
    get_object_or_404(Note,pk=id).delete()
    return redirect('home')

