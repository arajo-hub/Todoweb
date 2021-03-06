from django.db import models
from django.urls import reverse

class Todo(models.Model):
    todo=models.CharField(max_length=100)
    todo_done=models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse("todo:todo_list")

    def __str__(self):
        return self.todo
