from django.contrib import admin
from .models import Post
from .models import blog
from .models import Video
from .models import Userprofile,Comment,SubComment,Categories,FeedBack
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title"]
    class Meta:
        model = Post
admin.site.register(Post,PostModelAdmin)
admin.site.register(blog)
admin.site.register(Video)
admin.site.register(Userprofile)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Categories)
admin.site.register(FeedBack)







