from django.shortcuts import render
from . models import Product  # Assuming you have a Product model defined in models.py
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html')



def list_products(request):
    # Here you would typically fetch products from the database
    # For now, we'll just render a placeholder template
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)

    products = Product.objects.all()  # Fetch all products from the database
    product_paginator = Paginator(products, 4)  # Show 10 products per page
    product_list = product_paginator.get_page(page)
    context = {
        'products': product_list
    }
    return render(request, 'products.html', context)

def detail_products(request):
    # Here you would typically fetch the product from the database using the product_id
    # For now, we'll just render a placeholder template
    return render(request, 'product_detail.html')