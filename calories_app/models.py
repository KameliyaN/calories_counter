from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    kg = models.FloatField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Foods(models.Model):
    name = models.CharField(max_length=50)
    calories = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class CustomerFoods(models.Model):
    name = models.CharField(max_length=50, null=True)
    cust = Customer.objects.first().id if Customer.objects.first() else 1
    user = models.ForeignKey(to=Customer, on_delete=models.CASCADE, default=cust)
