from django.urls import path
from . import views
from .import api_views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('edit/<int:pk>', views.task_update, name='task-update'),
    path('delete/<int:pk>', views.task_delete, name='task-delete'),

    path('tasks/', api_views.TaskListCreateView.as_view(), name='api_task_list_create'),
    path('tasks/<int:pk>', api_views.TaskRetrieveUpdateDestroyView.as_view(), name='api_task_detail')

]