from django.shortcuts import render , redirect
from . models import notes 
from django.urls import reverse
from . forms import *
from django.contrib import messages
from django.views import generic


# Create your views here.
def home(request):
    return render(request , 'dashboard/home.html')

def note(request):
    if request.method =="POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = notes(user = request.user , title = request.POST['title'] , description = request.POST['description'])
            note.save()
        messages.success(request , f"Notes Succesfully created by  : {request.user.username}")
        
    else:
        form = NotesForm()
        
    allnote = notes.objects.filter(user = request.user)
    context = {"notes": allnote , "form": form}
    
    return render(request , 'dashboard/notes.html' , context) 


def delete(request , pk = None):
    
    notes.objects.get(id = pk).delete()
    return redirect('notes')

class  NotesDetailView(generic.DetailView):
    model = notes