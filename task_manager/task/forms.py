# task_manager/forms.py

from django import forms
from .models import Task, TaskImage

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'priority', 'completed')
# task_manager/forms.py

class TaskImageForm(forms.ModelForm):
    class Meta:
        model = TaskImage
        fields = ('image',)

class TaskFilterForm(forms.Form):
    title = forms.CharField(required=False, label='Title')
    created_at = forms.DateField(required=False, label='Creation Date', widget=forms.DateInput(attrs={'type': 'date'}))
    due_date = forms.DateField(required=False, label='Due Date', widget=forms.DateInput(attrs={'type': 'date'}))
    priority = forms.IntegerField(required=False, label='Priority')
    completed = forms.BooleanField(required=False, label='Completed', widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
