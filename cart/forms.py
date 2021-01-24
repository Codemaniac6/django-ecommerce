from django import forms
from django.utils.translation import gettext_lazy as _

ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddItemForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=ITEM_QUANTITY_CHOICES,
                                      coerce=int,
                                      label=_('Quantity'))

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)


class CartAddItemNoForm(forms.Form):
    quantity = 1

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
