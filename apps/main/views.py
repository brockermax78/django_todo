from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import Todoserializer

@api_view(['GET'])
def list_todos(request):
    todos = Todo.objects.all()
    serializer = Todoserializer(todos,many=True)
    return Response(serializer.data)
    # return Response({'msg':f'Hello i`am list_todos caller with method {request.method}'})

@api_view(['POST'])
def create_todos(request):
    serializers = Todoserializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
    # Todo(body='hello bitch').save()
        return Response(serializers.data)


@api_view(['DELETE'])
def delete_todos(request,pk):
    todo = get_object_or_404(Todo,id=pk)
    todo.delete()
    return Response(f'удалена запись под ключом {pk}')

@api_view(['PATCH'])
def update_todo(request,primary_key):
    todo = get_object_or_404(Todo,id=primary_key)
    serializer = Todoserializer(instance=todo, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
        # return Response(f'обновлена запись под ключем {primary_key}')