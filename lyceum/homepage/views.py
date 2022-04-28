from django.shortcuts import render

from catalog.models import Item
from django.views.generic import TemplateView


class Home(TemplateView):
    TEMPLATE = "homepage/home.html"

    def get(self, request, *args, **kwargs):
        items = Item.objects.published_items_with_tags()
        context = {
            "items": items,
        }
        return render(request, self.TEMPLATE, context)
