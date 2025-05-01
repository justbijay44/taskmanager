from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed')
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    deadline = models.DateTimeField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
