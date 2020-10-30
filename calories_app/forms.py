from django import forms

from calories_app.models import Customer, CustomerFoods


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerFoodsForm(forms.ModelForm):
    class Meta:
        model = CustomerFoods
        fields = ['food']
