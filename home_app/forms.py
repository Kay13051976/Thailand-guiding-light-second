from django import forms
from .models import Post,VISIBILITY


class UserPostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title']



class AccountForm(forms.Form):
    profileimage = forms.ImageField(label="Profile Image",required=False)
    accountname = forms.CharField(label="Account Name",max_length=100)
    first_name = forms.CharField(label="Firstame",max_length=30)
    last_name = forms.CharField(label="Lastname",max_length=30)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=15,label="Phone Number",)