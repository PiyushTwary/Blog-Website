from django.contrib import admin
from home.models import Post, UserInfo, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(UserInfo)
admin.site.register(Category)

