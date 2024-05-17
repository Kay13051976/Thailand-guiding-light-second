from django import forms
from .models import Post, VISIBILITY, Comment, User, Profile

from allauth.account.forms import SignupForm


class UserPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title']


class AccountForm(forms.Form):
    profileimage = forms.ImageField(label="Profile Image", required=False)
    accountname = forms.CharField(label="Account Name", max_length=100)
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=15, label="Phone Number",)


class CustomSignupForm(SignupForm):
    """Overwrite class to custom sign up form"""
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'comment']


class CommentsFormEdit(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'comment']
