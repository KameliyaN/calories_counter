from django.urls import path

from calories_app import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('foods/', views.customer_foods, name='customer-food'),
    path('details/<int:pk>/', views.details, name='details')

]
