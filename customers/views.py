from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
def account(request):
    if request.method == 'POST' and "login" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Logging in user:", username, password)

    elif request.method == 'POST' and "register" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        user = User.objects.create_user(username=username, password=password, email=email)
        print("Registering user:", username, password, email, address, phone)
        
    return render(request, 'account.html')

def logout_view(request):
    logout(request)
    return redirect('index')
