from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def taskList(request):
    task = {"name":"mock data meeting","age":26}
    return Response(task)