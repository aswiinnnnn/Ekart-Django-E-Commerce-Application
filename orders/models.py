from django.db import models
from customers.models import Customer
from products.models import Product

# models for orders


class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'),)

    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = (
        (ORDER_CONFIRMED, 'Order Confirmed'),
        (ORDER_PROCESSED, 'Order Processed'),
        (ORDER_DELIVERED, 'Order Delivered'),
        (ORDER_REJECTED, 'Order Rejected'),
    )

    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderedItem(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'),)

    small = 1
    medium = 2
    large = 3
    x_large = 4
    xx_large = 5
    SIZE_CHOICES = (
        (small, 'Small'),
        (medium, 'Medium'),
        (large, 'Large'),
        (x_large, 'X-Large'),
        (xx_large, 'XX-Large'),
    )
    
    
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    size = models.IntegerField(choices=SIZE_CHOICES, default=medium)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')