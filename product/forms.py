from django.shortcuts import render, redirect
from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # field = ['product_id', 'product_name', 'product_price', 'category']