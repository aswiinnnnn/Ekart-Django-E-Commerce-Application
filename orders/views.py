from django.shortcuts import render

# Create your views here.
def show_cart(request):
    # Here you would typically fetch cart items from the database
    # For now, we'll just render a placeholder template
    return render(request, 'cart.html')