from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.decorators import login_required
from note.models import Note
from taggit.models import Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from random import choice , randint
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

@login_required(login_url='/login/')
def home(request):
    currentUser = request.user
    print(currentUser)
    notes = Note.objects.all().filter(author=currentUser).order_by('-created_at')
    print(notes)
    common_tags = Note.tags.most_common()[:50]
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
        'tags':common_tags,
        'color':['primary','secondary','success','danger', 'warning', 'info'],
    }
    return render(request,'home.html',context=context)
@login_required(login_url='/login/')
def search(request):
    query = request.GET['search']
    notes = Note.objects.filter(title__contains=query, author=request.user)
    context = {
        'notes':notes,
        'query':query,
    }
    print(query)
    return render(request,'search.html',context)
@login_required(login_url='/login/')
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    print(tag)
    # Filter posts by tag name  
    posts = Note.objects.filter(tags=tag,author= request.user)
    context = {
        'tag':tag,
        'notes':posts,
        'color':['primary','secondary','success','danger', 'warning', 'info'],
    }
    return render(request, 'note/tags.html', context)