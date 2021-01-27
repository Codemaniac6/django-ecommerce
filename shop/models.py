from django.db import models
from django.urls import reverse

# CATEGORY_CHOICES = (
#     ('AR', 'Arts and Crafts'),
#     ('AU', 'Automotive'),
#     ('B', 'Baby'),
#     ('BP', 'Beauty and personal care'),
#     ('BK', 'Books'),
#     ('CM', 'Computers'),
#     ('DM', 'Digital music'),
#     ('E', 'Electronics'),
#     ('W', 'Women\'s fashion'),
#     ('M', 'Men\'s fashion'),
#     ('G', 'Girl\'s fashion'),
#     ('BY', 'Boy\'s fashion'),
#     ('HH', 'Health and household'),
#     ('HK', 'Home and kitchen'),
#     ('ID', 'industrial and scientific'),
#     ('L', 'Luggage'),
#     ('MT', 'Movies and Tv'),
#     ('S', 'Software'),
#     ('SO', 'Sports and outdoor'),
#     ('TH', 'Tools and Home improvement'),
#     ('TG', 'Toys and games'),
#     ('VG', 'Video games and accessories')
#                     )

LABEL_CHOICES = (
    ('S', 'secondary'),
    ('P', 'primary'),
    ('D', 'danger'),
)

TAG_CHOICES = (
    ('Best Seller', 'Best Seller'),
    ('NEW', 'NEW'),
    ('HOT', 'HOT')
)


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_list',
                       args=[self.slug])


class Item(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.CharField(choices=TAG_CHOICES,
                            max_length=20, blank=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_detail',
                       args=[self.id, self.slug])
