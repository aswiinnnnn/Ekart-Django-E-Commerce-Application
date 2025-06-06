from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('products/', views.list_products, name='list_products'),
   path('detail_product/<pk>/', views.detail_products, name='detail_products'),
]