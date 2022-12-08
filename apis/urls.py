from django.urls import path
from .views import taskList

urlpatterns = [
    path("task-list/",taskList,name="task-list"),
]