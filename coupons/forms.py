from django import forms
from .models import Coupon


class CouponApplyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ))
        # widget = {
        #     'code': forms.TextInput(
        #         attrs={'class': 'form-control'}
        #     )
        # }
