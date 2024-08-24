# urls.py
from django.urls import path
from .views import car_price_prediction

urlpatterns = [
    path('car-price/', car_price_prediction, name='car_price_prediction'),
]
