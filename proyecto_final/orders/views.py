from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from accounts.models import UserProfile
from products.models import Product
from orders.models import Order
from .models import *
from .cart import Cart

# Create your views here.
def cart_summary(req):
    return render(req, 'summary.html', {})
def cart_add(req):
    cart = Cart(req)
    if req.POST.get('action') == 'post':
        product_id = int(req.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        # response = JsonResponse({'Product': product.name})
        cart_quantity = cart.__len__()
        response =JsonResponse({'quantity': cart_quantity})
        return response
    return JsonResponse({'error': 'Invalid request'}, status=400)
def cart_delete(req):
    return render(req, 'cart_delete.html', {})




def create_order(req, product_id):
    if req.method == 'POST':
        get_product = get_object_or_404(Product, id=product_id)
        try:
            get_order = Order.objects.get(product=get_product)
            
        except Order.DoesNotExist:
            user_profile = get_object_or_404(UserProfile, name=req.user)
            get_order = Order.objects.create(
                product=get_product,
                customer=user_profile,
                address="",
                phone="",
                date=datetime.date.today(),
                quantity=1,
                status=False
            )
        return render(req, 'checkout.html', {'order':get_order})
    
def order_success(req):
    return render(req,'orders/order_success.html')