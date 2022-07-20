from django.contrib import admin
from .models import Task, Project, ProjectTask

# Register your models here.


admin.site.register((Task, Project, ProjectTask))
