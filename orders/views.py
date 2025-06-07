from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Order, OrderedItem  # Assuming these models are defined in models.py
from products.models import Product
from customers.models import Customer


# Create your views here.
@login_required(login_url='account')  # Ensure the user is logged in to access this view
def show_cart(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer_profile
            cart_obj, created = Order.objects.get_or_create(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            
            # Calculate subtotals for each item
            cart_items = []
            total_price = 0
            for item in cart_obj.added_items.all():
                subtotal = item.product.price * item.quantity
                total_price += subtotal
                cart_items.append({
                    'item': item,
                    'subtotal': subtotal
                })
            
            # Calculate tax and final price
            tax = total_price * 0.18  # 18% tax
            final_price = total_price + tax
            
            context = {
                'cart': cart_obj,
                'cart_items': cart_items,
                'total_price': total_price,
                'tax': tax,
                'final_price': final_price
            }
            return render(request, 'cart.html', context)
        else:
            messages.error(request, 'Please login to view your cart')
            return redirect('login')
    except Customer.DoesNotExist:
        messages.error(request, 'Please complete your profile to view cart')
        return redirect('account')
    except Exception as e:
        messages.error(request, f'Error loading cart: {str(e)}')
        return redirect('index')


@login_required(login_url='account')
def add_to_cart(request):
    # Logic to add a product to the cart
    if request.method == 'POST':
        user = request.user
        customer = user.customer_profile
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        size = int(request.POST.get('size', 2))
        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer, 
            order_status=Order.CART_STAGE
        )
        
        ordered_item = OrderedItem.objects.create(
            product_id=product_id,
            quantity=quantity,
            size=size,
            owner=cart_obj
        )
        messages.success(request, "Item added to cart successfully.")
        return redirect('cart')
    
    return redirect('cart')  # Redirect to cart page if not POST

@login_required(login_url='account')
def remove_from_cart(request, item_id):
    try:
        item = OrderedItem.objects.get(id=item_id)
        # Verify that the item belongs to the user's cart
        if item.owner.owner == request.user.customer_profile:
            item.delete()
            messages.success(request, "Item removed from cart successfully.")
        else:
            messages.error(request, "You don't have permission to remove this item.")
    except OrderedItem.DoesNotExist:
        messages.error(request, "Item not found in cart.")
    except ObjectDoesNotExist:
        messages.error(request, "Please complete your profile before accessing the cart.")
        return redirect('account')
    
    return redirect('cart')