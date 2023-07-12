from .models import Task
from django.forms import ModelForm, TextInput, Select


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'priority', 'status']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter the name'}),
            'description': TextInput(attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter the description'}),
            'deadline': TextInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'date',
                                         'placeholder': 'Enter the deadline'}),
            'priority': Select(attrs={ 'class': 'form-select', 'id': 'priority'}),
            'status': Select(attrs={'class': 'form-select', 'id': 'status'})
        }