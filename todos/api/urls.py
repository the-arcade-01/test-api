from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.apiOverview, name = "api-overview"),
    path('todo-list/',views.todolist, name = "todo-list"),
    path('todo-detail/<str:id>',views.tododetail, name = 'todo-detail'),
    path('todo-create/',views.todocreate, name = 'todo-create'),
    path('todo-update/<str:id>',views.todoupdate, name = 'todo-update'),
    path('todo-delete/<str:id>',views.tododelete, name = 'todo-delete'),
]
