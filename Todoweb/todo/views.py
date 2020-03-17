from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .forms import TodoForm, doneForm
from . import models

class CreatetodoView(LoginRequiredMixin, CreateView):
    login_url='/login/'
    redirect_field_name='todo/todo_list.html'
    form_class=TodoForm
    model=Todo

class todoListView(ListView):
    context_object_name='todos'
    model=models.Todo

    def get_queryset(self):
        return Todo.objects.filter(todo_done=False)

class todoDetailView(DetailView):
    context_object_name='tododetails'
    model=models.Todo
    template_name='todo/detail.html'

class todoUpdateView(LoginRequiredMixin, UpdateView):
    login_url='/login/'
    redirect_field_name='todo/detail.html'
    form_class=doneForm
    model=Todo

class doneUpdateView(LoginRequiredMixin, UpdateView):
    template_name='todo/detail.html'
    login_url='/login/'
    redirect_field_name='todo/todo_list.html'
    form_class=doneForm
    model=Todo
