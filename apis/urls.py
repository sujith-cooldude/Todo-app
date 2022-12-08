from django.urls import path
from .views import taskList, taskDetail, taskUpdate, taskCreate

urlpatterns = [
    path("task-list/", taskList, name="task-list"),
    path("task-detail/<str:pk>", taskDetail, name="task-detail"),
    path("task-update/<str:pk>", taskUpdate, name="task-update"),
    path("task-create/", taskCreate, name="task-create"),
]
