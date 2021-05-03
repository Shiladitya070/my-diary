from django.shortcuts import render

# Create your views here.

def show(request,id):
    return render(request,'note/show-note.html')


def edit(request,id):
    return render(request,'note/edit-note.html')


def delete(request,id):
    # Backend Logic here
    pass