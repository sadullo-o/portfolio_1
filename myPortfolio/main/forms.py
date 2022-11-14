from django import forms
from .models import Contact, MyUsers, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class AddContact(forms.Form):
#     name = forms.CharField(max_length=200)
#     email = forms.CharField(max_length=250)
#     subject = forms.CharField(max_length=250)
#     message = forms.CharField(max_length=350)

class AddContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class CreateUsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog', 'username']