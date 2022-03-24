from django.contrib import admin
from catalog.models import catalog_item, catalog_tag, catalog_category


@admin.register(catalog_item)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'category', 'is_published')
    list_editable = ('is_published',)
    filter_horizontal = ('tegs',)


@admin.register(catalog_tag)
class CatalogTagAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_published')
    list_editable = ('is_published',)


@admin.register(catalog_category)
class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'weight', 'is_published')
    list_editable = ('is_published',)

