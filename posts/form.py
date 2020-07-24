from django import forms
from .models import blog
from django_ckeditor_5.widgets import CKEditor5Widget
class PostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = [
            "title",
            "content",
        ]