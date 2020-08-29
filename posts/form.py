from django import forms
from .models import Post
from .models import blog
from .models import Userprofile
from .models import Userprofile
from django_ckeditor_5.widgets import CKEditor5Widget
from taggit.managers import TaggableManager
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "tags",
            "draft",
            "categories"
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "tags": forms.TextInput(attrs={'class':'form-control'}),
            "categories": forms.Select(attrs={'class':'form-control'}),
            "content": CKEditor5Widget()
            
        }
class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = [
            "phone",
            "birth",
            "profession",
            "about_me",
            "profile_img",
        ]
        widgets = {
            "profession": forms.TextInput(attrs={'class':'form-control'}),
            "about_me": forms.Textarea(attrs={'class':'form-control'}),
            "birth": forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            "phone":forms.NumberInput(attrs={'class':'form-control'}),
        }