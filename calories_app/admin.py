from django.contrib import admin

# Register your models here.
from calories_app.models import Customer, Foods, CustomerFoods

admin.site.register(Customer)
admin.site.register(Foods)
admin.site.register(CustomerFoods)

