from django import forms
from Todo.models import TaskModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDescription']
        # fields = '__all__'