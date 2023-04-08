from django.contrib import admin
from .models import Project, Post, Like
list = [Post, Like]

admin.site.register(list)
