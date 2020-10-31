from django.shortcuts import render, redirect

# Create your views here.
from calories_app.forms import CustomerForm, CustomerFoodsForm
from calories_app.models import Customer, CustomerFoods, Foods


def index(request):
    if Customer.objects.all():
        if request.method == 'POST':
            form = CustomerFoodsForm(request.POST)

            if form.is_valid():
                form.cust = form.save()
                form.cust.save()
                return redirect('customer-food')

            return render(request, 'calories_app/home-with-profile.html', {'form': form})
        form = CustomerFoodsForm()
        return render(request, 'calories_app/home-with-profile.html', {'form': form})
    else:
        form = CustomerForm()
        return render(request, 'calories_app/home-no-profile.html', {'form': form})


def customer_foods(request):
    return render(request, 'calories_app/customer_foods.html')
