from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('category/<str:cat_name>', views.CategoryProducts.as_view(), name='category'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:product_id>/', views.remove_item, name='item_clear'),
    path('cart/item_increment/<int:product_id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:product_id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.view_cart ,name='cart'),
    path('order/success', views.submit_order, name='order')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)