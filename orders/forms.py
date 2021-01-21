from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'country']
        widget = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', }
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'address': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'postal_code': USZipCodeField(),
            'city': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'country': forms.TextInput(
                attrs={'class': ' form-control'}
            ),
        }
