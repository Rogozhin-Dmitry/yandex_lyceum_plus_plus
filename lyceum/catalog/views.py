from django.shortcuts import get_object_or_404, render

from catalog.models import Item


def item_list(request):
    items = Item.objects. \
        filter(is_published=True). \
        prefetch_related('tags'). \
        only('name', 'text', 'tags')
    template = 'catalog/item_list.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request, item_num):
    item = get_object_or_404(Item.objects.
                             select_related('category').
                             only('name', 'text', 'category'), id=item_num)
    context = {
        'item': item,
    }
    template = 'catalog/item_detail.html'
    return render(request, template, context)
