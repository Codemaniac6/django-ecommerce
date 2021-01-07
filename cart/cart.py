from decimal import Decimal
from django.conf import settings
from shop.models import Item


class Cart(object):

    def __init__(self, request):
        """
        Initializes the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # saves an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the items from the database.
        """
        item_ids = self.cart.keys()
        # Get the Item object and add them to cart
        items = Item.objects.filter(id__in=item_ids)

        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item'] = item

        for product in cart.values():
            product['price'] = Decimal(product['price'])
            product['total_price'] = product['price'] * product['quantity']
            yield product

    def add(self, item, quantity=1, override_quantity=False):
        """
        Adds an item to the cart or updates it quantity
        """
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0,
                                  'price': str(item.price)}
        if override_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def __len__(self):
        """
        Counts all items in the cart
        """
        return sum(product['quantity'] for product in self.cart.values())

    def save(self):
        # marks the session as "modified" to make sure it gets saved.
        self.session.modified = True

    def remove(self, item):
        """
        Remove an item from the cart
        """
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(product['price']) * product['quantity'] for product in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
