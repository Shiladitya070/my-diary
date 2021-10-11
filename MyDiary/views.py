from django.http.response import Http404
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from note.models import Note
from taggit.models import Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import View
from MyDiary.utils import render_to_pdf



def home(request):

    return render(request,'home.html')
def About(request):

    return render(request,'About.html')
def Contact(request):

    return render(request,'contact.html')

def GeneratePdf(request, slug, *args, **kwargs):
        note = get_object_or_404(Note, slug=slug)
        context = {
            'note': note,
        }
        
        pdf = render_to_pdf('note/pdf-notes.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"Mynotes_{note.title}.pdf"
            content = f"inline; filename={filename}"
            download = request.GET.get("download")
            if download:
                content = f"attachment; filename={filename}"
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
       





@login_required(login_url='/login/')
def mynotes(request):
    currentUser = request.user

    notes = Note.objects.all().filter(author=currentUser).order_by('-created_at')

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
    return render(request,'mynotes.html',context=context)

@login_required(login_url='/login/')
def search(request):
    query = request.GET['search']
    notes = Note.objects.filter(title__contains=query, author=request.user)
    context = {
        'notes':notes,
        'query':query,
    }
    return render(request,'search.html',context)
@login_required(login_url='/login/')
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Note.objects.filter(tags=tag,author= request.user)
    context = {
        'tag':tag,
        'notes':posts,
        'color':['primary','secondary','success','danger', 'warning', 'info'],
    }
    return render(request, 'note/tags.html', context)