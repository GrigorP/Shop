from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('cart/', CartPageListView.as_view(), name='cart'),
    path('checkout/', CheckoutPageListView.as_view(), name='checkout'),
    path('contact/', ContactPageListView.as_view(), name='contact'),
    path('shop/', ShopPageListView.as_view(), name='shop'),
    path('product/<int:id>', ProductDetailView.as_view(), name='product'),
    path('shop/latest', ShopPageLatestListView.as_view(), name='latest'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
]

