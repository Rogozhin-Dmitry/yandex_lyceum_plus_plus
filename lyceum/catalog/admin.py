from django.contrib import admin
from catalog.models import Item, Tag, Category


@admin.register(Item)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'category', 'is_published')
    list_editable = ('is_published',)
    filter_horizontal = ('tags',)


@admin.register(Tag)
class CatalogTagAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_published')
    list_editable = ('is_published',)


@admin.register(Category)
class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_published')
    list_editable = ('is_published',)
