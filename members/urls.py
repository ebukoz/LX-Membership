from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('cars/', views.cars, name='cars'),
    path('cars/cardetails/<int:id>', views.cardetails, name='cardetails'),
]