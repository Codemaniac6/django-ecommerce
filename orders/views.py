from django.shortcuts import render
from .models import OrderItem, Order
from cart.cart import Cart
from .forms import OrderCreateForm


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        order = Order(request.POST)
        if order:
            for product in cart:
                OrderItem.objects.create(order=order,
                                         item=product['item'],
                                         price=product['price'],
                                         quantity=product['quantity'])
                cart.clear()
                return render(request, 'orders/order/created.html',
                              {'order': order,
                               'cart': cart})
    else:
        order = Order()
        return render(request, 'checkout-page.html',
                      {'order': order,
                       'cart': cart})
        # form = OrderCreateForm(request.POST)
        # if form.is_valid():
        #     order = form.save()
        #     for product in cart:
        #         OrderItem.objects.create(order=order,
        #                                  item=product['item'],
        #                                  price=product['price'],
        #                                  quantity=product['quantity'])
        #         # clears the cart.
    #             cart.clear()
    #             return render(request, 'orders/order/created.html',
    #                           {'order': order})
    # else:
    #     form = OrderCreateForm()
    #     return render(request, 'checkout-page.html',
    #                   {'cart': cart,
    #                    'form': form})
