from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=('todo',)

        dic={
            'todo':forms.TextInput()
        }

class doneForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=('todo_done',)

        dic={
            'todo_done':forms.CheckboxInput()
        }
