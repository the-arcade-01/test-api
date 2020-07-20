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

@api_view(['GET'])
def tododetail(request,id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(todo,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def todocreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def todoupdate(request,id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(instance=todo,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def tododelete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response(f"Item of index {id} is deleted successfully!")
