from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
from django.contrib.auth.models import User
import datetime
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
# Create your models here. 
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)    
    title = models.CharField(max_length=400)
    slug = models.SlugField(unique=True)
    email = models.EmailField()
    content = CKEditor5Field(blank=True,null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    draft = models.BooleanField(default=False)
    tags = TaggableManager()
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/post-detail/" %(self.slug)
    def total_likes(self):
        return self.likes.count()
    class Meta:
        ordering = ["-timestamp","-updated"] 
def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug 
def create_email(instance,new_email=None):
    email = instance.user
    return email
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if not instance.email:
        instance.email = create_email(instance)
pre_save.connect(pre_save_post_receiver,sender=Post)

# Create your models here.
class blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)    
    title = models.CharField(max_length=400)
    content = RichTextField(blank=True,null=True)
class Video(models.Model):
    url = models.CharField(max_length=800)
class Userprofile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)    
    phone = models.IntegerField(blank=True,null=True)
    username = models.CharField(max_length=100,unique=True)
    birth = models.DateField(blank=True,null=True)
    profession = models.CharField(max_length=800,blank=True,null=True)
    about_me = models.TextField(blank=True,null=True)
    profile_img = models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.username
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    comm = models.TextField()
class SubComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    comm = models.TextField()   
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    