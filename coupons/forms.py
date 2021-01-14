from django import forms


class CouponApplyForm(forms.ModelForm):
    code = forms.CharField()
