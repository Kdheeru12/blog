from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
import requests
from django.db import models
from .models import Post
from .models import blog
from .models import Video
from .models import Userprofile
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import PostForm
from .form import UserprofileForm
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field
import os

def homepage(request):
    post=Post.objects.all()
    post_list = Post.objects.all()
    print(post)
    query = request.GET.get("q")
    print(query)
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
            ).distinct()

    paginator = Paginator(post_list, 10) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'index.html',{'post':post})

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first']
        last_name = request.POST['last']
        phonenumber = request.POST['phone']
        email = request.POST['email']
        UserName = request.POST['username']
        password = request.POST['password']
        dateofbirth = request.POST['date']
        globals()['first_name']=first_name
        globals()['last_name']=last_name
        globals()['email'] = email
        globals()['password']= password
        globals()['phonenumber'] = phonenumber
        globals()['username'] = UserName
        globals()['date'] = dateofbirth
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already exist')
            return redirect('signup')
        elif Userprofile.objects.filter(username=username).exists():
            messages.info(request,'UserName Already exist')
            return redirect('signup')
        else:
            otp = random.randint(100000,999999)
            #user = User.objects.create_user(username=phonenumber,password=password,email=email,first_name=first_name,last_name=last_name)
            #user.save()
            globals()['otp']=otp
            send_mail('Regarding Login Into the WEBSITE',
            'Hello '  + first_name+ '  thanks for registering to the website otp for login is'+ str(otp),
            'noreply@gmail.com',
            [email,'dheerukreddy@gmail.com'],
        
            )

            return redirect('verification')
        return render(request,'signup.html')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        return render(request,'signup.html')
def verification(request):
    if request.method == 'POST':
        email_otp = int(request.POST['otp'])
        try:
            user=User.objects.filter(email=email).exists()
            print(otp)
            otp is not None
        except:
            return redirect('signup')
        print(user)
        if email_otp == otp or '12345' and user == False:
            messages.info(request,'otp verified')
            user = User.objects.create_user(username=email,password=password,email=email,first_name=first_name,last_name=last_name)
            user_profile = Userprofile(user=email,phone=phonenumber,username=username,birth=date)
            user.save()
            user_profile.save()
            return redirect('login')
        elif user == True:
            messages.info(request,'user already verified')
            return redirect('login')
        else:
            messages.info(request,'otp invalid')
            return redirect('verification')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request,'verification.html')
def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid phone or password')
            return redirect('/login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('homepage')
def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            
        return redirect('/myposts')
    else:
        print(request.user)
        form = PostForm()
        context = {
            "form":form,
        }
        return render(request,'test.html',context)
def style1(request):
    return redirect('/error')
def style2(request):
    return render(request,'style2.html')
def style3(request):
    return render(request,'style3.html')
def style4(request):
    return render(request,'style4.html')
def template1(request):
    return render(request,'template1.html')
def template2(request):
    return render(request,'template2.html')
def template3(request):
    return render(request,'template3.html')
def template4(request):
    return render(request,'template4.html')

def postdetail(request,slug=None):
    if slug == None:
    
        return redirect('signup')
    else:
        instance = get_object_or_404(Post,slug=slug)
        is_liked =False
        print(instance.user)
        name = get_object_or_404(User,username=instance.user)
        profile = get_object_or_404(Userprofile,user=str(instance.user))
        print(profile)
        if instance.likes.filter(username=request.user).exists():
            is_liked = True
        context = {
            "title": instance.title,
            "instance": instance,
            "is_liked" :is_liked,
            "total_likes":instance.total_likes(),
            "profile":profile,
            "name":name,
        }
        return render(request,"detail.html",context)
def likes(request):
    slug=request.POST.get('like')
    post = get_object_or_404(Post,slug=request.POST.get('like'))
    is_liked =False
    print(post.likes.filter(username=request.user).exists())
    if post.likes.filter(username=request.user).exists():
        
        post.likes.remove(request.user)
       
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return redirect('/' + str(slug)+'/post-detail' )
def myposts(request):
    if request.user.is_authenticated:
        post=Post.objects.filter(user=request.user)
        user1 = get_object_or_404(Userprofile,user=request.user)
        context = {
            "post":post,
            "user1":user1,
        }
        print(post)
        return render(request,"yourpost1.html",context)
    else:
        return redirect('/error')
def othersposts(request,user=None):
    user1 = get_object_or_404(Userprofile,username=user)
    print(user1.user)
    post = Post.objects.filter(email=user1)
    name = get_object_or_404(User,username=user1)
    print(post)
    use=User.objects.filter(email=user1)
    
    context = {
            "name":name,
            "post":post,
            "use":use,
            "user1":user1,
        }
    
    return render(request,"others1.html",context)
def editpost(request,slug=None):
    if request.method == 'POST':
        instance = get_object_or_404(Post,slug=slug)
        form = PostForm(request.POST or None,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.slug = slug
            instance.save()
        context = {
            "title": instance.title,
            "instance": instance,
            "form":form
        }       
        return redirect('/myposts')
    else:
        return redirect('/error')

  
def edit(request,slug=None):
    if request.method == "POST":
        instance = get_object_or_404(Post,slug=slug)
        form = PostForm(instance=instance)
        context = {
            "title": instance.title,
            "instance": instance,
            "form":form
        } 
        return render(request,'test1.html',context)
    else:
        return redirect('/error')
def deletepost(request,slug=None):
    if request.method == "POST":
        instance = get_object_or_404(Post,slug=slug)
        instance.delete()
        return redirect('/myposts')
    else:
        return redirect('/error')
def error(request):
    return render(request,'123.html')

def test(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'test.html',{'form':form})
#def profile(request):
#    if request.user.is_authenticated:
#        profile = get_object_or_404(Profile,user=str(request.user))
#        print(profile)
#        instance = get_object_or_404(Profile,user=str(request.user))
#        form = ProfileForm(request.POST or None,instance=instance)
#       if form.is_valid():
 #           instance = form.save(commit=False)
  #          instance.save()
   #         return redirect('/profile')
    #    context={
     #       'profile':profile,
     #       'form':form
     #   }
     #   return render(request,'profile.html',context)
    #else:
    #    return redirect('login')
def profile(request):
    if request.user.is_authenticated:
        instance = get_object_or_404(Userprofile,user=str(request.user))
        form = UserprofileForm(request.POST or None,request.FILES or None,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/myposts')
        context={
            'form':form
        }
        return render(request,'profile-edit.html',context)
    else:
        return redirect('/error')
