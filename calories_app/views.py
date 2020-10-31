from django.http import HttpResponse
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
    customer = Customer.objects.first()
    return render(request, 'calories_app/customer_foods.html', {'customer': customer})


def details(request, pk):
    customer = Customer.objects.first()
    food_name = customer.customerfoods_set.get(pk=pk).name
    foods_list = Foods.objects.all()
    searched_object = [x for x in foods_list if x.name.lower() == food_name.lower()]
    print(searched_object)

    context = {
        'food': searched_object[0]
    }

    return render(request, 'calories_app/details.html', context)


def delete(request, pk):
    customer = Customer.objects.first()
    food_obj = customer.customerfoods_set.get(pk=pk)
    food_obj.delete()
    return redirect('customer-food')
