from random import sample

from django.shortcuts import render
from django.db.models import Prefetch

from catalog.models import Item, Tag

from Core.constants import NUMBER_DISPLAYED_ITEMS_ON_MAIN_PAGE


def home(request):
    item_values_list = (
        Item.objects.filter(is_published=True)
        .all()
        .values_list("id", flat=True)
    )

    items = (
        Item.objects.filter(
            pk__in=sample(list(item_values_list),
                          NUMBER_DISPLAYED_ITEMS_ON_MAIN_PAGE)
        )
        .prefetch_related(
            Prefetch(
                "tags", queryset=Tag.objects
                .filter(is_published=True)
                .only("name")
            )
        )
        .only("name", "text", "tags")
    )
    TEMPLATE = "homepage/home.html"
    context = {
        "items": items,
    }
    return render(request, TEMPLATE, context)
