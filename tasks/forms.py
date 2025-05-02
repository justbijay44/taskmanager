from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline' ,'assignee', 'status']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required")
        return title
    
    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if not deadline:
            raise forms.ValidationError("Deadline is requied")
        return deadline