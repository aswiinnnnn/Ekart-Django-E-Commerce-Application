from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Order, OrderedItem  # Assuming these models are defined in models.py
from products.models import Product
from customers.models import Customer
from datetime import date, timedelta


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
            tax = total_price * 0.6  # 18% tax
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
        size = request.POST.get('size')  # Get size as string first
        
        # Convert size to integer if provided, otherwise keep as None
        size = int(size) if size else None
        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer, 
            order_status=Order.CART_STAGE
        )

        # Check if the item already exists in cart
        try:
            # If size is None, only check product_id
            if size is None:
                ordered_item = OrderedItem.objects.get(
                    owner=cart_obj,
                    product_id=product_id,
                    size__isnull=True
                )
            else:
                ordered_item = OrderedItem.objects.get(
                    owner=cart_obj,
                    product_id=product_id,
                    size=size
                )
            # Update quantity if item exists
            ordered_item.quantity += quantity
            ordered_item.save()
        except OrderedItem.DoesNotExist:
            # Create new item if it doesn't exist
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


@login_required(login_url='account')
def checkout(request):
    if request.method == 'POST':
        user = request.user
        customer = user.customer_profile
        total = float(request.POST.get('total')) # Convert to float to handle decimal val
        cart_obj= Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
        if cart_obj.added_items.exists():
            # Update order status to ORDER_CONFIRMED
            cart_obj.order_status = Order.ORDER_CONFIRMED
            cart_obj.final_price = total  # Save the final price to the order object
            cart_obj.address = customer.address
            cart_obj.save()
            messages.success(request, "Order confirmed successfully.")

            # Calculate estimated delivery date (e.g., 5 days from now)
            estimated_delivery_date = date.today() + timedelta(days=5)
            
            context = {
                'order': cart_obj,  # Pass the actual Order object
                'order_items': cart_obj.added_items.all(),
                'estimated_delivery_date': estimated_delivery_date,
            }
            return render(request,'order_summary.html', context)
        else:
            messages.error(request, "Unable to confirm order. Some thing went wrong.")
            return redirect('cart')

