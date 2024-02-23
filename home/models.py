from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250) 
    body =  RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=250) 
    likes = models.ManyToManyField(User, related_name='liked_posts')
    dislikes = models.ManyToManyField(User, related_name='disliked_post')

    def __str__(self) -> str:
        return self.title

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilePic = models.ImageField(null=True,blank=True ,default='default.jpg',upload_to='ProfilePic/')
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    contact = models.CharField(null=True,max_length=14)

    def __str__(self) -> str:
        return self.name
