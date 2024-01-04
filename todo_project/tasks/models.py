from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    RECURRING_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  # Auto-set when the task is created
    due_date = models.DateField(null=True, blank=True)
    subtasks = models.ManyToManyField('self', symmetrical=False, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    tags = models.ManyToManyField(Tag, blank=True)
    reminder_time = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='task_attachments/', null=True, blank=True)
    notes = models.TextField(blank=True)
    recurring = models.CharField(max_length=10, choices=RECURRING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title
