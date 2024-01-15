from django import forms
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['title', 'description']
        
class DateInput(forms.DateInput):
    input_type = 'date'
  
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widget = {'due':DateInput()}
        fields = ['subject' , 'title', 'description' ,'due' ,'is_finished']
        
class Dashboardform(forms.Form):
    text = forms.CharField(max_length= 100 , label = "Enter Your Search : ")
    
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title' , 'is_finished']  
    