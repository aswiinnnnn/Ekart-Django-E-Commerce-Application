from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')



def list_products(request):
    # Here you would typically fetch products from the database
    # For now, we'll just render a placeholder template
    return render(request, 'products.html')

def detail_products(request, product_id):
    # Here you would typically fetch the product from the database using the product_id
    # For now, we'll just render a placeholder template
    return render(request, 'product_detail.html', {'product_id': product_id})