from django.db import models

from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

class Project(models.Model):
    title = CharField(max_length=80)
    description = CharField(max_length=250)
    image = ImageField(upload_to="blog/images/project")
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=300)
    content = CharField(max_length=5000, null=True)
    image = ImageField(upload_to="blog/images/blog")
    date = DateField(default=date.today)

    def __str__(self):
        return self.title
    
    
    
    
