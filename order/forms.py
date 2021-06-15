from django.shortcuts import render, redirect
from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # field = ['order_id', 'manager_id', 'date', 't_price']