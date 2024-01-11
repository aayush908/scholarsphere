from django import forms
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['title', 'description']
