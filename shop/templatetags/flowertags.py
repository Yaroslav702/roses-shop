from django import template
from shop.models import *
from cart.cart import Cart

register = template.Library()

@register.simple_tag()
def total(request, product_id):
    cart = Cart(request)
    return cart.total(product_id)


@register.simple_tag()
def get_total(request):
    cart = Cart(request)
    return cart.get_total()