from django.shortcuts import render

# Create your views here.
def account(request):
    # Here you would typically fetch customer account details from the database
    # For now, we'll just render a placeholder template
    return render(request, 'account.html')