from django.shortcuts import render

from catalog.models import Item


def home(request):
    items = Item.objects.published_items_with_tags()
    TEMPLATE = "homepage/home.html"
    context = {
        "items": items,
    }
    return render(request, TEMPLATE, context)
