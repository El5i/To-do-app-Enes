
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'tags', 'reminder_time', 'attachment', 'subtasks', 'notes', 'recurring']
