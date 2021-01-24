from django.shortcuts import render, get_object_or_404
from .models import Category, Item
from .recommender import Recommender
from cart.views import CartAddItemForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    paginator = Paginator(items, 8)     # 8 items in each page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        items = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver the last page
        items = paginator.page(paginator.num_pages)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     translations__slug=category_slug)
        items = items.filter(category=category)
    return render(request,
                  'item/list.html',
                  {'category': category,
                   'categories': categories,
                   'page': page,
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
