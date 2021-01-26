from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline
from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    inlines = [TranslationInline]
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Item)
class ItemAdmin(TranslatableAdmin):
    inlines = [TranslationInline,]
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
