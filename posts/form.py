from django import forms
from .models import Post
from .models import blog
from .models import Userprofile
from django_ckeditor_5.widgets import CKEditor5Widget
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
        }