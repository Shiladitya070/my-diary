from django.shortcuts import redirect,render
from note.models import Note


def home(request):
    notes = Note.objects.order_by('-created_at')
    context = {
        'notes': notes
    }
    return render(request,'home.html',context=context)
def search(request):
    query = request.GET['query']
    print(query)
    return render(request,'search.html')