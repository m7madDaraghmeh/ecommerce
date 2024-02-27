import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}  
    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'id': product.id,
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[i]["quantity"],
                'get_total': total
            }
            items.append(item)    
            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'cartItems':cartItems , 'order':order , 'items':items}



def cartData(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order, created=Order.objects.get_or_create(customer=customer , complete=False) #this function query an object if it doesnot created then create it 
        items = order.orderitem_set.all() #query the child object by setting parent value then the child object so it will give all orderitems that have the order variable as parent 
        cartItems= order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems  = cookieData['cartItems']
        order      = cookieData['order']
        items      = cookieData['items']
    return {'cartItems':cartItems , 'order':order , 'items':items}

def guestOrder(request ,data  ):
    print('user is not logged in')  

    print('COOKIES :' , request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
            email = email,
        )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer = customer ,
        complete = False
        )
    for item in items :
        product = Product.objects.get(id = item['product']['id'])

        orderItem = OrderItem.objects.create(
            product = product ,
            order = order ,
            quantity= item['quantity']
            )
    return customer ,order   