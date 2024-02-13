from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context={'products' : products}
    return render(request , 'store/store.html' , context)
def cart(request):

    if request.user.is_authenticated:
        customer= request.user.customer
        order, created=Order.objects.get_or_create(customer=customer , complete=False) #this function query an object if it doesnot created then create it 
        items = order.orderitem_set.all() #query the child object by setting parent value then the child object so it will give all orderitems that have the order variable as parent 
    else:
        items=[]
        order={ 'get_cart_total' : 0 , 'get_cart_items' : 0 }
    context={'items' : items , 'order' : order}
    return render(request , 'store/cart.html' , context)
def checkout(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order, created=Order.objects.get_or_create(customer=customer , complete=False) #this function query an object if it doesnot created then create it 
        items = order.orderitem_set.all() #query the child object by setting parent value then the child object so it will give all orderitems that have the order variable as parent 
    else:
        items=[]
        order={ 'get_cart_total' : 0 , 'get_cart_items' : 0 }
    context={'items' : items , 'order' : order}
    return render(request , 'store/checkout.html' , context)


