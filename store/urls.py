from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('detail/', views.detail, name="detail"),
    path('update_item/', views.updateItem, name="update_item"),
]