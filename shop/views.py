from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from .models import Product
from .form import CreateUserForm


@login_required(login_url='login')
def home(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'products-list.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.data['username']
            messages.success(request, f'Account "{user}" was successfully created')

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


class CategoryProducts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_objects(self, cat_name):
        try:
            return Product.objects.filter(category = cat_name)
        except:
            raise Http404
    

    def get(self, request, cat_name, *args, **kwargs):
        self.products = self.get_objects(cat_name)
        return Response({'cat_products': self.products}, template_name='category-products.html')


@login_required(login_url='login')
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('home')


@login_required(login_url='login')
def remove_item(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect('cart')


@login_required(login_url='login')
def item_increment(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('cart')


@login_required(login_url='login')
def item_decrement(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    try:
        cart.decrement(product=product)
    except:
        cart.remove(product)
    return redirect('cart')



@login_required(login_url='login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')


@login_required(login_url='login')
def view_cart(request):
    return render(request, 'cart.html')


@login_required(login_url='login')
def submit_order(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'order.html')