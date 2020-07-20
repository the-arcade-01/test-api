from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo

# rest_framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# importing serializers
from .serializers import TodoSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/todo-list/',
        'Detail View':'/todo-detail/<str:id>/',
        'Create':'/todo-create/',
        'Update':'/todo-update/<str:id>/',
        'Delete':'/todo-delete/<str:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def todolist(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos,many=True)
    return Response(serializer.data)