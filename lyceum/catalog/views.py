from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch

from catalog.models import Item, Tag


def item_list(request):
    items = (
        Item.objects.filter(is_published=True)
        .only("name", "text", "tags")
        .prefetch_related(
            Prefetch(
                "tags", queryset=Tag.objects
                .filter(is_published=True)
                .only("name")
            )
        )
    )
    TEMPLATE = "catalog/item_list.html"
    context = {
        "items": items,
    }
    return render(request, TEMPLATE, context)


def item_detail(request, item_num):
    item = get_object_or_404(
        Item.objects.select_related("category")
        .only("name", "text", "category")
        .prefetch_related(
            Prefetch(
                "tags", queryset=Tag.objects
                .filter(is_published=True)
                .only("name")
            )
        ),
        id=item_num,
    )
    context = {
        "item": item,
    }
    template = "catalog/item_detail.html"
    return render(request, template, context)
