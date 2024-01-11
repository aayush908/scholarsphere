from django.shortcuts import render
from . models import notes 
from . forms import *
# Create your views here.
def home(request):
    return render(request , 'dashboard/home.html')

def note(request):
    form = NotesForm()
    allnote = notes.objects.filter(user = request.user)
    context = {"notes": allnote , "form": form}
    
    return render(request , 'dashboard/notes.html' , context) 