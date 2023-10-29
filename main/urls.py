from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('cart/', CartPageListView.as_view(), name='cart'),
    path('checkout/', CheckoutPageListView.as_view(), name='checkout'),
    path('contact/', ContactPageListView.as_view(), name='contact'),
    path('shop/', ShopPageListView.as_view(), name='shop'),
    path('product/', ProductDetailView.as_view(), name='product'),
]