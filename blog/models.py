from django.db import models
from django.contrib.auth.models import User

from django.db.models.fields import CharField, DateField, URLField, TextField
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
    description = CharField(max_length=1000)
    content = TextField(max_length=6000, null=True)
    ilustration = ImageField(upload_to="blog/images/blog", null=True)
    continuation_of_content = TextField(max_length=6000, null=True)
    ilustration_2 = ImageField(upload_to="blog/images/blog", null=True)
    end_of_content = TextField(max_length=6000, null=True)
    image = ImageField(upload_to="blog/images/blog")
    date = DateField(default=date.today)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('post', 'user')
    
    