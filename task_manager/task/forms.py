# task_manager/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
# task_manager/forms.py

class TaskFilterForm(forms.Form):
    title = forms.CharField(required=False, label='Title')
    created_at = forms.DateField(required=False, label='Creation Date', widget=forms.DateInput(attrs={'type': 'date'}))
    due_date = forms.DateField(required=False, label='Due Date', widget=forms.DateInput(attrs={'type': 'date'}))
    priority = forms.IntegerField(required=False, label='Priority')
    completed = forms.BooleanField(required=False, label='Completed', widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
