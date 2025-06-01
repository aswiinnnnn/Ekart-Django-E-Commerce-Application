from django.shortcuts import render
from . models import Product  # Assuming you have a Product model defined in models.py

# Create your views here.
def index(request):
    return render(request, 'index.html')



def list_products(request):
    # Here you would typically fetch products from the database
    # For now, we'll just render a placeholder template
    products = Product.objects.all()  # Fetch all products from the database
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def detail_products(request):
    # Here you would typically fetch the product from the database using the product_id
    # For now, we'll just render a placeholder template
    return render(request, 'product_detail.html')