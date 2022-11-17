from django.contrib.auth.models import User
from django import forms
class Signupform(forms.ModelForm):
    # password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']

        widgets={
            "username":forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}),
            "email":forms.EmailInput(attrs={'placeholder':'Email'}),
            "password":forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}),
            "first_name":forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
            "last_name":forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),
            # "email":forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}),
            
        }

