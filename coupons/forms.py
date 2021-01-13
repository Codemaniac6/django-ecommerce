from django import forms


class CouponApplyForm(forms.MOdelForm):
    code = forms.CharField()
