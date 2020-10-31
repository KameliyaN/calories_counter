from django import forms
from django.forms import Select

from calories_app.models import Customer, CustomerFoods


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerFoodsForm(forms.ModelForm):
    # select_foods=forms.ChoiceField(choices=fo.name for fo in CustomerFoods.food.all())
    class Meta:
        model = CustomerFoods
        fields = ['name']
        exclude = ['cust','user']

