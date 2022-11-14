from django import forms
from .models import Blogs



class AddBlog(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'content']