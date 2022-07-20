from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    title =  models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ('-created',) #['complete']


class Project(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    title =  models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # deadline = models.DateTimeField()

    def __str__(self):
        return self.title

class ProjectTask(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null= True, blank=True)
    task_title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.task_title

    