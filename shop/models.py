from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORY_CHOICES = (
    ('AR', 'Arts and Crafts'),
    ('AU', 'Automotive'),
    ('B', 'Baby'),
    ('BP', 'Beauty and personal care'),
    ('BK', 'Books'),
    ('CM', 'Computers'),
    ('DM', 'Digital music'),
    ('E', 'Electronics'),
    ('W', 'Women\'s fashion'),
    ('M', 'Men\'s fashion'),
    ('G', 'Girl\'s fashion'),
    ('BY', 'Boy\'s fashion'),
    ('HH', 'Health and household'),
    ('HK', 'Home and kitchen'),
    ('ID', 'industrial and scientific'),
    ('L', 'Luggage'),
    ('MT', 'Movies and Tv'),
    ('S', 'Software'),
    ('SO', 'Sports and outdoor'),
    ('TH', 'Tools and Home improvement'),
    ('TG', 'Toys and games'),
    ('VG', 'Video games and accessories')
                    )

TAG_CHOICES = (
    ('S', 'secondary'),
    ('P', 'primary'),
    ('D', 'danger'),
)


# class Category(models.Model):
#     Arts_and_Crafts = 'AR'
#     Automotive = 'AU'
#     Baby = 'B'
#     Beauty_and_personal_care = 'BP'
#     Books = 'BK'
#     Computers = 'CM'
#     Electronics = 'E'
#     Women_fashion = 'W'
#     Men_fashion = 'M'
#     Girls_fashion = 'G'
#     Boys_fashion = 'BY'
#     Health_and_household = 'HH'
#     Home_and_kitchen = 'HK'
#     industrial_and_scientific = 'ID'
#     Luggage = 'L'
#     Movies_and_Tv = 'MT'
#     Software = 'S'
#     Sports_and_outdoor = 'SO'
#     Tools_and_Home_improvement = 'TH'
#     Toys_and_games = 'TG'
#     Video_games_and_accessories = 'VG'
#
#     CATEGORY_CHOICES = (
#         (Arts_and_Crafts, 'Arts and Crafts'),
#         (Automotive, 'Automotive'),
#         (Baby, 'Baby'),
#         (Beauty_and_personal_care, 'Beauty and personal care'),
#         (Books, 'Books'),
#         (Computers, 'Computers'),
#         (Electronics, 'Electronics'),
#         (Women_fashion, 'Women\'s fashion'),
#         (Men_fashion, 'Men\'s fashion'),
#         (Girls_fashion, 'Girl\'s fashion'),
#         (Boys_fashion, 'Boy\'s fashion'),
#         (Health_and_household, 'Health and household'),
#         (Home_and_kitchen, 'Home and kitchen'),
#         (industrial_and_scientific, 'industrial and scientific'),
#         (Luggage, 'Luggage'),
#         (Movies_and_Tv, 'Movies and Tv'),
#         (Software, 'Software'),
#         (Sports_and_outdoor, 'Sports and outdoor'),
#         (Tools_and_Home_improvement, 'Tools and Home improvement'),
#         (Toys_and_games, 'Toys and games'),
#         (Video_games_and_accessories, 'Video games and accessories')
#     )
#     name = models.CharField(choices=CATEGORY_CHOICES,
#                             max_length=20)
#     slug = models.SlugField(max_length=200,
#                             db_index=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('shop:item_list',
#                        args=[self.slug])
#

class Item(models.Model):
    # Arts_and_Crafts = 'AR'
    # Automotive = 'AU'
    # Baby = 'B'
    # Beauty_and_personal_care = 'BP'
    # Books = 'BK'
    # Computers = 'CM'
    # Electronics = 'E'
    # Women_fashion = 'W'
    # Men_fashion = 'M'
    # Girls_fashion = 'G'
    # Boys_fashion = 'BY'
    # Health_and_household = 'HH'
    # Home_and_kitchen = 'HK'
    # industrial_and_scientific = 'ID'
    # Luggage = 'L'
    # Movies_and_Tv = 'MT'
    # Software = 'S'
    # Sports_and_outdoor = 'SO'
    # Tools_and_Home_improvement = 'TH'
    # Toys_and_games = 'TG'
    # Video_games_and_accessories = 'VG'

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="items/%d/%m/%Y", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.CharField(choices=TAG_CHOICES, max_length=1, blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.id, self.slug])