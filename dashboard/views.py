from django.shortcuts import render
from . models import notes

# Create your views here.
def home(request):
    return render(request , 'dashboard/home.html')

def note(request):
    allnote = notes.objects.filter(user = request.user)
    context = {"notes": allnote}
    print(context)
    return render(request , 'dashboard/notes.html' , context)