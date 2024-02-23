from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.register, name="register"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('uploadInfo', views.uploadInfo, name="uploadInfo"),
    path('editProfile/<int:pk>', views.editProfile, name="editProfile"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('reset', views.reset, name="reset"),
    path('users', views.users, name="users"),
    path('userDetail/<int:pk>', views.userDetail, name="userDetail"),
    path('addcats', views.addcats, name="addcats"),
    path('catPage/<str:category>', views.catPage, name="catPage"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete/<int:pk>', views.delPost, name="delete"),
    path('createBlog', views.createBlog, name="createBlog"),
    path('like/<int:pk>', views.like, name="like"),
    path('dislike/<int:pk>', views.dislike, name="dislike"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
