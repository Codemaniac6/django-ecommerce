import redis
from django.conf import settings
from .models import Item

# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


class Recommender(object):

    @staticmethod
    def get_item_key(id):
        return f'item:{id}:purchased_with'

    def items_bought(self, items):
        item_ids = [item.id for item in items]
        for item_id in item_ids:
            for with_id in item_ids:
                # get the other product bought with each product
                if item_id != with_id:
                    # increment score for product purchased together
                    r.zincrby(self.get_item_key(item_id), 1, with_id)

    def suggest_product_for(self, items, max_result=6):
        item_ids = [item.id for item in items]
        if len(items) == 1:
            # only one product
            suggestions = r.zrange(self.get_item_key(item_ids[0]), 0, -1, desc=True)[:max_result]
        else:
            # generate a temporary key
            flat_ids = ''.join([str(id) for id in item_ids])
            tmp_key = f'tmp_{flat_ids}'
            # multiple items, combine score of all items
            # store the resulting sorted set in a temporary key
            keys = [self.get_item_key(id) for id in item_ids]
            r.zunionstore(tmp_key, keys)
            # remove ids for items the recommendation is for.
            r.zrem(tmp_key, *item_ids)
            # get the item ids by their score, descendant sort
            suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_result]
            # remove the temporary key
            r.delete(tmp_key)
        suggested_item_ids = [int(id) for id in suggestions]
        # get suggested items and sort by order of appearance
        suggested_items = list(Item.objects.filter(id__in=suggested_item_ids))
        suggested_items.sort(key=lambda x: suggested_item_ids.index(x.id))
        return suggested_items

    def clear_purchases(self):
        for id in Item.objects.value_list('id', flat=True):
            r.delete(self.get_item_key(id))
