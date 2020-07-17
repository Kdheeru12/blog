from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from .models import Post
import requests
from django.db import models
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import PostForm

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
        password = request.POST['password']
        globals()['first_name']=first_name
        globals()['last_name']=last_name
        globals()['email'] = email
        globals()['password']= password
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already exist')
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
            fail_silently=True,
            )

            return redirect('verification')
        return render(request,'signup.html')
    else:
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
        if email_otp == otp and user == False:
            messages.info(request,'otp verified')
            user = User.objects.create_user(username=email,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('login')
        elif user == True:
            messages.info(request,'user already verified')
            return redirect('login')
        else:
            messages.info(request,'otp invalid')
            return redirect('verification')
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
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('homepage')
def createpost(request):
    if request.method == 'POST':
        title = request.POST["title"]
        template = request.POST["template"]
        content = request.POST["content"]
        email = request.POST["email"]
        user = request.user
        if template == 'style1':
            print(title , template ,content) 
            instance = Post(title=title,template_name=template,content=content,email=email,user=user)
            instance.save()       
        elif template =='style2':
            heading1 = request.POST["heading1"]
            para = request.POST["para"]
            heading2 = request.POST["heading2"]
            content1 = request.POST["content1"]
            heading3 = request.POST["heading3"]
            content2 = request.POST["content2"]
            instance = Post(title=title,template_name=template,content=content,email=email,user=user,heading1=heading1,para1=para,heading2=heading2,heading3=heading3,content1=content1,content2=content2)
            instance.save()
                  
        elif template =='style3':
            heading1 = request.POST["heading1"]
            heading2 = request.POST["heading2"]
            content1 = request.POST["content1"]
            heading3 = request.POST["heading3"]
            content2 = request.POST["content2"]
            heading4 = request.POST["heading4"]
            content3 = request.POST["content3"]
            instance = Post(title=title,template_name=template,content=content,email=email,user=user,heading1=heading1,heading2=heading2,heading3=heading3,content1=content1,content2=content2,heading4=heading4,content3=content3)
            instance.save()
        elif template =='style4':
            heading1 = request.POST["heading1"]
            para = request.POST["para"]
            instance = Post(title=title,template_name=template,content=content,email=email,user=user,heading1=heading1,para1=para)
            instance.save()       
        return redirect('/myposts')
    else:
        return render(request,'post.html')
def style1(request):
    return redirect('/error')
def style2(request):
    return render(request,'style2.html')
def style3(request):
    return render(request,'style3.html')
def style4(request):
    return render(request,'style4.html')
def template1(request):
    return render(request,'template3.html')
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
        
        if instance.likes.filter(username=request.user).exists():
            is_liked = True
        context = {
            "title": instance.title,
            "instance": instance,
            "is_liked" :is_liked,
            "total_likes":instance.total_likes(),
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
        return render(request,"myposts.html",{'post':post})
    else:
        return redirect('/error')
def othersposts(request,user=None):
    post=Post.objects.filter(email=user)
    user=User.objects.filter(email=user)
    context = {
            
            "post":post,
            "user":user
        }
    print(post)
    return render(request,"others.html",context)
def editpost(request,slug=None):
    if request.method == "POST":
        like = []
        instance = get_object_or_404(Post,slug=slug)
        globals()['likes']= instance.likes.all()
        print('likes:',likes)
        print('like:',like)
        for users in likes:
            print(users)
            like.append(users)
        globals()['users']=list(like)

        context = {
            "title": instance.title,
            "instance": instance,
        }

        return render(request,'edit.html',context)
    else:
        return redirect('/error')
  
def save(request,slug=None):
    if request.method == "POST":
        instance = get_object_or_404(Post,slug=slug)
        title = request.POST["title"]
        template = request.POST["template"]
        content = request.POST["content"]
        email = request.POST["email"]
        user = request.user
        para = request.POST["para"]
        heading1 = request.POST["heading1"]
        heading2 = request.POST["heading2"]
        content1 = request.POST["content1"]
        heading3 = request.POST["heading3"]
        content2 = request.POST["content2"]
        heading4 = request.POST["heading4"]
        content3 = request.POST["content3"]
        instance.delete()
        print('likes:',users)
        instance = Post(title=title,template_name=template,content=content,email=email,user=user,heading1=heading1,heading2=heading2,heading3=heading3,content1=content1,content2=content2,heading4=heading4,content3=content3,para1=para)
        instance.save()
        post = get_object_or_404(Post,slug=slug)
        for likes in users:
            post.likes.add(likes)
        return redirect('/'+str(slug)+'/post-detail' )
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
    return render(request,'error.html')