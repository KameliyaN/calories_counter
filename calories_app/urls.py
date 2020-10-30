from django.urls import path

from calories_app import views

urlpatterns = [
    path('', views.index, name='index_page')

]
