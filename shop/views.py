from django.shortcuts import render, get_object_or_404
from .models import Category, Item
from cart.views import CartAddItemForm


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
    return render(request,
                  'item/list.html',
                  {'category': category,
                   'categories': categories,
                   'items': items})


def item_detail(request, id, slug):
    item = get_object_or_404(Item,
                             id=id,
                             slug=slug,
                             available=True)
    cart_item_form = CartAddItemForm
    return render(request,
                  'product-page.html',
                  {'item': item,
                   'cart_item_form': cart_item_form})
