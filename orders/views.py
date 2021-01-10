from django.shortcuts import render, redirect
from .models import OrderItem
from cart.cart import Cart
from .forms import OrderCreateForm
from .tasks import order_created
from django.urls import reverse


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for product in cart:
                OrderItem.objects.create(order=order,
                                         item=product['item'],
                                         price=product['price'],
                                         quantity=product['quantity'])
                # clears the cart.
            cart.clear()
            # launches asynchronous task
            order_created.delay(order.id)
            # set the order in the session.
            request.session['order_id'] = order.id
            # redirect for payment.
            return redirect(reverse('payment: process'))
    else:
        form = OrderCreateForm()
    return render(request, 'checkout-page.html',
                  {'cart': cart,
                   'form': form})
