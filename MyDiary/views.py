from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.decorators import login_required
from note.models import Note
from taggit.models import Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def home(request):
    
    notes = Note.objects.order_by('-created_at')
    common_tags = Note.tags.most_common()[:4]
    page = request.GET.get('page',1)
    paginator = Paginator(notes, 8)
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)


    context = {
        'notes': notes,
        'tags':common_tags
    }
    return render(request,'home.html',context=context)
def search(request):
    query = request.GET['search']
    notes = Note.objects.filter(title__contains=query)
    context = {
        'notes':notes,
        'query':query,
    }
    print(query)
    return render(request,'search.html',context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Note.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)