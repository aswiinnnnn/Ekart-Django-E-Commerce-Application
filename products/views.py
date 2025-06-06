from django.shortcuts import render
from . models import Product  # Assuming you have a Product model defined in models.py
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    freatured_products = roducts = Product.objects.order_by("-priority")[:8]  # Fetch the top 8 products based on priority
    latest_products = roducts = Product.objects.order_by("-id")[:8]  # Fetch the latest 8 products
    context = {
        'freatured_products': freatured_products,
        'latest_products': latest_products
    }

    return render(request, 'index.html', context)



def list_products(request):
    # Here you would typically fetch products from the database
    # For now, we'll just render a placeholder template
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)

    products = Product.objects.order_by("-priority")  # Fetch all products from the database
    product_paginator = Paginator(products, 8)  # Show 10 products per page
    product_list = product_paginator.get_page(page)
    context = {
        'products': product_list
    }
    return render(request, 'products.html', context)

def detail_products(request,pk):

    product_detail = Product.objects.get(pk=pk)  # Fetch the product by primary key
    context = {
        'product': product_detail
    }
    # Here you would typically fetch the product from the database using the product_id
    # For now, we'll just render a placeholder template


    return render(request, 'product_detail.html', context)