from random import randint

from django.shortcuts import render

from catalog.models import Item


def home(request):
    item_values_list = Item.objects. \
        filter(is_published=True). \
        all(). \
        values_list('id', flat=True)
    if len(item_values_list) < 3:
        pass
        items = Item.objects. \
            filter(pk__in=item_values_list). \
            prefetch_related('tags'). \
            only('name', 'text', 'tags')
    else:
        random_item_id = randint(0, len(item_values_list) - 3)
        items = Item.objects. \
            filter(pk__in=item_values_list[
                          random_item_id:random_item_id + 3]). \
            prefetch_related('tags'). \
            only('name', 'text', 'tags')
    template = 'homepage/home.html'
    context = {
        'items': items,
    }
    return render(request, template, context)
