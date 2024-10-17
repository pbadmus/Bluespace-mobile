from django import forms

class MakeForm(forms.Form):
    name = forms.CharField(max_length=255, label="Brand Name")
    logo = forms.URLField(required=False, label="Brand Logo URL")
    is_phone = forms.BooleanField(required=False, label="Phone")
    is_television = forms.BooleanField(required=False, label="Television")
    is_laptop = forms.BooleanField(required=False, label="Laptop")
    is_wearable = forms.BooleanField(required=False, label="Wearable")
