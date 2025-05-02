from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task

class TaskSeriazliers(serializers.ModelSerializer):
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'deadline', 'assignee', 'status','created_at', 'modified_at']