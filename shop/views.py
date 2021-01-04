from django.shortcuts import render, get_object_or_404
from .models import Category, Item


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
    item =get_object_or_404(Item,
                            id=id,
                            slug=slug,
                            available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'item': item})