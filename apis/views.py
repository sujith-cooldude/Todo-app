from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from base.models import Task

@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def taskDetail(request,pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def taskUpdate(request,pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
