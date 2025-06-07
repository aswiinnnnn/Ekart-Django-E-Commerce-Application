from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='account')  # Ensure the user is logged in to access this view
def show_cart(request):
    # Here you would typically fetch cart items from the database
    # For now, we'll just render a placeholder template
    return render(request, 'cart.html')