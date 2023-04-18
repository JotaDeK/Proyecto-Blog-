from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe
from .models import Project, Post, Like
list = [Post, Like, Project]

class PostAdminForm(forms.ModelForm):
    texto = forms.CharField(required=False, widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = '__all__'

admin.site.register(list, form=PostAdminForm)
