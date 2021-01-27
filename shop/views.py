from django.shortcuts import render, get_object_or_404
from .models import Category, Item
from .recommender import Recommender
from cart.views import CartAddItemForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    paginator = Paginator(items, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)

    return render(request,
                  'item/list.html',
                  {'category': category,
                   'categories': categories,
                   'page_obj': page_obj,
                   'items': items})


def item_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    item = get_object_or_404(Item,
                             id=id,
                             translations__language_code=language,
                             translations__slug=slug,
                             available=True)
    cart_item_form = CartAddItemForm

    r = Recommender()
    recommended_products = r.suggest_product_for([item], 4)

    return render(request,
                  'product-page.html',
                  {'item': item,
                   'cart_item_form': cart_item_form,
                   'recommended_products': recommended_products})
