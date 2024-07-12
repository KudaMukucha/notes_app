from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Note
# Create your views here.
@login_required
def notes(request):
    notes = Note.objects.filter(is_deleted = False,user =request.user)
    # print(notes)
    return render(request,'dashboard/index.html',{'notes':notes})

@login_required
def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Note.objects.create(user = request.user, title=title,description=description)
        return redirect('dashboard')
    else:
        return render(request,'dashboard/add-note.html')
    

@login_required
def edit_note(request,pk):
    get_note = get_object_or_404(Note,pk=pk)
    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']
        get_note.title = new_title 
        get_note.description = new_description
        get_note.save()
        return redirect('dashboard')
    else:
        return render(request,'dashboard/note.html',{'get_note':get_note})
    
def move_to_trash(request,pk):
     note = get_object_or_404(Note,pk=pk)
     note.is_deleted = True
     note.save()
     return redirect('dashboard')

def restore_note(request,pk):
    note = get_object_or_404(Note,pk=pk)
    note.is_deleted = False
    note.save()
    return redirect('trash')

def notes_trash(request):
    trash_notes = Note.objects.filter(is_deleted = True,user = request.user)
    return render(request,'dashboard/trash.html',{'notes':trash_notes})


def delete_note(request,pk):
     note = get_object_or_404(Note,pk=pk)
     note.delete()
     return redirect('trash')
