from django.db import models
from psycopg2 import Date


# Create your models here.
class Task(models.Model):
    class Priority(models.TextChoices):
        High = 'A'
        Medium = 'B'
        Low = 'C'

    class Status(models.TextChoices):
        In_progress = 'In progress'
        Awaiting = 'Awaiting'
        Completed = 'Completed'

    name: str = models.CharField(max_length=100)
    description: str = models.TextField()
    deadline: Date = models.DateField()
    priority: str = models.CharField(max_length=6, choices=Priority.choices, default=Priority.High.name)
    status: str = models.CharField(max_length=20, choices=Status.choices, default=Status.In_progress.name)
