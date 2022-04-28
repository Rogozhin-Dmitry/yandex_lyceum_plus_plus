from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from catalog.models import Category, ImageModel, Item, Tag


@admin.register(Item)
class CatalogItemAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "small_text",
        "category",
        "is_published",
        "admin_image",
    )
    list_editable = ("is_published",)
    filter_horizontal = (
        "tags",
        "images",
    )


@admin.register(Tag)
class CatalogTagAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published")
    list_editable = ("is_published",)


@admin.register(Category)
class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published")
    list_editable = ("is_published",)


@admin.register(ImageModel)
class CatalogImageModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        'img_preview',
    )
