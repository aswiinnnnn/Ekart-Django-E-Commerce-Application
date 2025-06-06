from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from . models import Customer  # Assuming you have a Customer model defined in models.py
from django.contrib import messages

# Create your views here.
def account(request):

    if request.method == 'POST' and "login" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    elif request.method == 'POST' and "register" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            customer = Customer(user=user, address=address, phone=phone)
            customer.save()
            return redirect('index')
        
   


        
        
    return render(request, 'account.html')

def logout_view(request):
    logout(request)
    return redirect('index')
