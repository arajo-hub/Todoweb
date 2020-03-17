from django.urls import path
from . import views

app_name='todo'

urlpatterns=[
    path('', views.todoListView.as_view(), name='todo_list'),
    path('create/', views.CreatetodoView.as_view(), name='createtodo'),
    path('<int:pk>/detail/', views.todoDetailView.as_view(), name='detail'),
    path('<int:pk>/', views.todoUpdateView.as_view(), name='todoedit'),
    path('<int:pk>/done/', views.doneUpdateView.as_view(), name='doneedit'),
]
