from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Post, UserInfo, Category
from home.forms import ImageForm, PostForm
from django.urls import reverse

#Admin @dmin1234

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    all_post = Post.objects.all().order_by('-pk')
    all_cats = Category.objects.all()
    context = {
        "posts" : all_post,
        "cats": all_cats
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if len(password)<8:
            messages.error(request, "Password must be 8 Characters long")
            return redirect('register')
        get_all_users = User.objects.filter(username = username)
        if get_all_users:
            messages.error(request,"Username already Exists!!!")
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        new_user = authenticate(request, username=username, password=password)
        login(request,new_user)
        messages.success(request, 'Registration Successful, Please fill the form below')
        return redirect("uploadInfo")
    return render(request, 'register.html')

def uploadInfo(request):
    if not request.user.is_authenticated:
        messages.error(request, "Login to Access the Website!!!")
        return redirect('login')
    if request.method =="POST":
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.user = request.user
            image.email = request.user.email
            image.save()
            return redirect('home') 
    else:
        image_form = ImageForm()
    return render(request, "uploadInfo.html", {'image_form': image_form})

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect("login")    
    return render(request, 'login.html')

def reset(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if len(password) < 8:
            messages.error(request, "Password must be 8 Characters long")
            return redirect('reset')
        elif not User.objects.filter(username=username, email=email).exists():
            messages.error(request, username+" Username does not exists")
            return redirect('reset')
        user = User.objects.get(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "Password RESET succesful")
        return redirect('login')
    return render(request, 'reset.html')

def createBlog(request):
    if not request.user.is_authenticated:
        messages.error(request, "Login to Access the Website!!!")
        return redirect('login')
    post_form = PostForm(request.POST)
    if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "BLOG POSTED SUCCESSFULLY!")
            return redirect('home')
    return render(request, 'createBlog.html', {'post_form': post_form})

def addcats(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        messages.error(request, "Login to Access the Website!!!")
    if request.method == "POST":
        cat = request.POST.get("cat")
        new_cat = Category(name = cat)
        new_cat.save()
        messages.success(request, "NEW CATEGORY ADDED SUCCESSFULLY!!!")
        return redirect('home')
    return render(request, 'adcats.html')

def catPage(request, category):
    all_posts = Post.objects.filter(category = category)
    all_cats = Category.objects.all()
    context = {
        "posts" : all_posts,
        "cats": all_cats
    }
    return render(request, 'catPage.html', context)

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "BLOG EDITED SUCCESSFULLY!!!")
            return redirect('detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})

def delPost(request, pk):
    get_post = Post.objects.get(pk = pk)
    get_post.delete()
    messages.success(request, "BLOG DELETED SUCCESSFULLY!!!")
    return redirect('home')

def detail(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Login to Access the Website!!!")
        return redirect('login')
    get_post = Post.objects.filter(pk=pk)
    print(get_post)
    context = {
        "posts": get_post
    }
    return render(request, 'detail.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('login')

def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "Login to Access the Website!!!")
        return redirect('login')
    user  = request.user
    get_posts = Post.objects.filter(author=user).order_by('-pk')
    get_info = UserInfo.objects.filter(user = user)
    context={
        "posts": get_posts,
        "userInfo": get_info
    }
    return render(request, 'dashboard.html', context)

def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        if user in post.dislikes.all():
            post.dislikes.remove(user)
        post.likes.add(user)
    return redirect('detail', pk=pk)

def dislike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if user in post.dislikes.all():
        post.dislikes.remove(user)
    else:
        if user in post.likes.all():
            post.likes.remove(user)
        post.dislikes.add(user)
    return redirect('detail', pk=pk)

def editProfile(request,pk):
    if not request.user.is_authenticated:
        messages.error(request, "Login to Access the Website!!!")
        return redirect('login')
    userinfo = get_object_or_404(UserInfo, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=userinfo)
        if form.is_valid():
            if 'profilePic' in request.FILES:  
                userinfo.profilePic = request.FILES['profilePic']
            messages.success(request, "PROFILE UPDATED SUCCESSFULLY!!!")
            form.save() 
            return redirect('dashboard')
    else:
        form = ImageForm(instance=userinfo)
    return render(request, 'editProfile.html', {'form': form, 'userinfo':userinfo})

def users(request):
    users = UserInfo.objects.all()
    return render(request, 'users.html', {'users': users})

def userDetail(request, pk):
    user = UserInfo.objects.get(pk = pk)
    return render(request, 'userDetail.html', {'users': user})