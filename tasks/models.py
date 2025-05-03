from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver

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

@receiver(post_save, sender=Task)
def send_task_notification(sender, instance, created, **kwargs):
    if created and instance.assignee.email:
        subject= f'New Assigned Task: {instance.title}'
        message= f'Hi {instance.assignee.username}, You have been assigned a new task : {instance.title}'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.assignee.email],
            fail_silently=False,
        )