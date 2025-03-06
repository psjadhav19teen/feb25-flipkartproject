from django import forms
from .models import Address,Product

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=["mobile","address","pincode"]

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            "userid",
            "productid",
            "productname",
            "category",
            "description",
            "price",
            "images"
        ]