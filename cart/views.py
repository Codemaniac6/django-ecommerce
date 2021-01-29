from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Item
from shop.recommender import Recommender
from coupons.forms import CouponApplyForm
from .cart import Cart
from .forms import CartAddItemForm
from django.contrib import messages


@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
        messages.info(request, "Item added to cart")
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    messages.info(request, "Item removed from cart")
    if cart:
        return redirect('cart:cart_detail')
    return redirect('/')


def cart_detail(request):
    cart = Cart(request)
    for product in cart:
        product['update_quantity_form'] = CartAddItemForm(initial={
            'quantity': product['quantity'],
            'override': True
        })
    coupon_apply_form = CouponApplyForm()

    r = Recommender()
    cart_products = [product['item'] for product in cart]
    recommended_products = r.suggest_product_for(cart_products, max_result=4)

    return render(request,
                  'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form,
                   'recommended_products': recommended_products})
