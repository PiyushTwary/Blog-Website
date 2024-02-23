from django.db import models
from django.forms import fields
from .models import UserInfo, Category, Post
from django import forms

choices = Category.objects.all().values_list('name','name')
choice_list = []
for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "category", "body"]

        widgets = {
            "category": forms.Select(choices=choice_list)
        }

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = UserInfo
        fields = ["profilePic","name","contact"]
