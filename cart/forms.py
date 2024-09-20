from django import forms


class AddToProductForm(forms.Form):
    QUANTITY_CHOICE = [str(i) for i in range(1, 30)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE, coerce=int)
