from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


# Create your views here.
def product_list(req):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 10)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(req, 'product_list.html',{'page_obj': page_obj})
    
def product_detail(req, product_id):
    product = Product.objects.get(id=product_id)
    return render(req, 'product_detail.html',{'product':product})