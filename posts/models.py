from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)    
    title = models.CharField(max_length=400)
    slug = models.SlugField(unique=True)  
    email = models.EmailField()
    image = models.ImageField(blank=True,null=True)
    heading1 = models.CharField(max_length=400,null=True)
    para1    = models.TextField(null=True)
    content = models.TextField()
    heading2 = models.CharField(max_length=400,null=True)
    content1 = models.TextField(null=True)
    heading3 = models.CharField(max_length=400,null=True)
    content2 = models.TextField(null=True)
    heading4 = models.CharField(max_length=400,null=True)
    content3 = models.TextField(null=True)
    
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True)
    template_name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
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
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver,sender=Post)