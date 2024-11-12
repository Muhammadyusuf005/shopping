from django.urls import path

from apps.orders.views import checkout
from config.urls import urlpatterns

urlpatterns = [
    path('',checkout,name='checkout-page'),
]