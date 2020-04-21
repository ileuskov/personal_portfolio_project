from django.contrib import admin

# add some models from models.py
from .models import Project

admin.site.register(Project)

