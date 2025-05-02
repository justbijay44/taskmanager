from django.urls import path
from .import api_views

urlpatterns = [
    path('tasks/', api_views.TaskListCreateView.as_view(), name='api_task_list_create'),
    path('tasks/<int:pk>', api_views.TaskRetrieveUpdateDestroyView.as_view(), name='api_task_detail')
]