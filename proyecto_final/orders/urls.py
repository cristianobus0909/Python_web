from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/<int:product_id>/', create_order, name='checkout' ),
    path('success/', order_success, name= 'order_success'),
    path('sumary/', cart_summary, name= 'cart_summary'),
    path('add/', cart_add, name= 'cart_add'),
    path('delete/', cart_delete, name= 'cart_delete'),
]