from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=['customer_name','email','phone']
        widgets ={
            'customer_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Customer Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'})
        }
