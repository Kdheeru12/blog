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
from django.core.paginator import Paginator
from django.shortcuts import render

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

    paginator = Paginator(post_list, 1) # Show 25 contacts per page.
    
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
          
            return redirect("/homepage")
            
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
        print(title , template ,content) 
        instance = Post(title=title,template_name=template,content=content,email=email)
        instance.save()       
        return redirect('homepage')
       
    else:
        return render(request,'post.html')
def style1(request):
    return render(request,'template1.html')
def postdetail(request,slug=None):
    if slug == None:
    
        return redirect('signup')
    else:
        instance = get_object_or_404(Post,slug=slug)
        context = {
            "title": instance.title,
            "instance": instance,
        }
        return render(request,"detail.html",context)
def error(request):
    return render(request,'error.html')