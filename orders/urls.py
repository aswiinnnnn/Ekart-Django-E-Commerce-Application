from django.urls import path
from . import views

urlpatterns = [
   path('cart/', views.show_cart, name='cart'),
   path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
   path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
   path('checkout/',views.checkout,name='checkout'),
   

]