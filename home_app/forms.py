from django import forms
from .models import Post, VISIBILITY

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

    # password1 = forms.CharField(
    # widget=forms.PasswordInput, label='Password',min_length=8)
    # password2 = forms.CharField(
    # widget=forms.PasswordInput, label='Confirm Password',min_length=8)
