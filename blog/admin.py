from django.contrib import admin
from django import forms
from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe
from .models import Project, Post, Like
list = [Post, Like]

admin.site.register(list)
