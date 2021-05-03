from django.shortcuts import redirect,render,get_object_or_404
from note.models import Note
from taggit.models import Tag


def home(request):
    
    notes = Note.objects.order_by('-created_at')
    context = {
        'notes': notes
    }
    return render(request,'home.html',context=context)
def search(request):
    query = request.GET['search']
    print(query)
    return render(request,'search.html')

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Note.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)