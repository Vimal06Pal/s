from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('', views.index),
    path('uploadproduct',views.view_product,name="uploadproduct"),
    path('category',views.add_category,name="category"),
    path('allproduct',views.all_products,name="allproduct"),
    path('upload',views.upload_multiImage,name="upload"),
    path('signup',views.signup_handle,name="signup"),
    path('login',views.login_handle,name="login"),
    path('logout', views.logoutUser,name="logout"),
    path('productview/<str:name>',views.productview,name = "productview"),
    # path("addcomment",views.addcomments,name="addcomment"),
    path("check",views.check_pincode,name="check"),
    path("add_to_cart",views.add_to_cart,name="add_to_cart"),
    path("cartpage/<int:id>",views.cartpage,name="cartpage"),
    path("quantity",views.quantity_add,name="quantity"),
    path("add_item",views.add_item,name="item_add"),
    path("remove_item",views.remove_item,name="remove_add"),
    path("add_item_cart",views.add_item_cart,name="item_add_cart"),
    path("remove_item_cart",views.remove_item_cart,name="remove_add_cart"),













]