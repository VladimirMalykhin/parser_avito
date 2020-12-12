from django.db import models

# Create your models here.
class Task(models.Model):
    phrase = models.CharField(max_length=255)
    region = models.CharField(max_length=100)


class Result(models.Model):
    task = models.ForeignKey(Task, related_name="task", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=15, default="")
