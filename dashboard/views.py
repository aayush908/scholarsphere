from django.shortcuts import render , redirect
from . models import *
from django.urls import reverse
from . forms import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
import requests


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
    
    
def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
                    
            except:
                finished = False
            homework = Homework(user = request.user , subject = request.POST['subject'] , title = request.POST['title'] , description = request.POST['description'] , due = request.POST['due'] , is_finished = finished)
            homework.save()
            messages.success(request , f"Homework Added successfully from :{request.user.username}")
        
    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user = request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    
    context = {"homeworks": homework , 'homework_done': homework_done , 'form':form}
   
    return render(request , 'dashboard/homework.html' , context) 

def update_homework(request , pk = None):
    homework = Homework.objects.get(id = pk)
    print(homework)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
        
    homework.save()
    return redirect('homework')

def delete_homework(request , pk = None):
    Homework.objects.get(id = pk).delete()
    return redirect('homework')
    
def youtube(request ):
    if request.method =="POST":
        form = Dashboardform(request.POST)
        text = request.POST['text']
        video = VideosSearch(text , limit = 10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
                    }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text'] 
            result_dict['description'] = desc
            result_list.append(result_dict)
            context ={'form':form, 'results':result_list}
        return render(request , 'dashboard/youtube.html' , context)
    else:
        form = Dashboardform()
    context = {'form':form}
    return render(request, 'dashboard/youtube.html' , context)

def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            try:
                finished = request.POST["is_finished"]
                if finished == "on":
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todos = Todo(user = request.user, title =request.POST['title'] , is_finished = finished )
            todos.save()
            messages.success(request ,f"Todo added from :{request.user.username} ")
    else:
              
        form = TodoForm()
    alldata = Todo.objects.filter(user = request.user)
    if len(alldata) == 0:
        todo_done = True
    else:
        todo_done = False
    context = {'alldata':alldata , 'form':form ,'todo_done':todo_done}
    return render(request , 'dashboard/todo.html' , context)

def update_todo(request , pk = None):
    todo = Todo.objects.get(id = pk)
    print(todo)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
        
    todo.save()
    return redirect('todo')

def delete_todo(request , pk = None):
    Todo.objects.get(id = pk).delete()
    return redirect('todo')
    
    
def books(request):
    if request.method == "POST":
        form = Dashboardform(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')
            
            }
            result_list.append(result_dict)
        context = {'form':form , 'results':result_list}
        return render(request, 'dashboard/books.html' , context)
    
    else:
        
        form = Dashboardform()
    context = {'form':form}
    return render(request , 'dashboard/books.html' , context)

def dictionary(request):
    if request.method == "POST":
        form = Dashboardform(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            
            context = {
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition, 
                'example':example,
                'synonyms':synonyms
            }
            
        except:
            context = {
                'form':form,
                'input':''
                
            }
        
        return render(request , "dashboard/dictionary.html", context)
          
    else:
        form = Dashboardform()
    context = {'form':form}
    return render(request , 'dashboard/dictionary.html' , context )   