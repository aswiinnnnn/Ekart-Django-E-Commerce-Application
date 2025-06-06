from django.urls import path
from . import views

urlpatterns = [
   path('account/', views.account, name='account'),
   path('logout/', views.logout_view, name='logout'),
]