from django.shortcuts import get_object_or_404, render

from catalog.models import Item


def item_list(request):
    items = Item.objects.published_items_with_category_name_and_weight()
    categories = {}
    categories_list = []
    for item in items:
        if (item.category.name, item.category.weight) in categories:
            categories[(item.category.name, item.category.weight)].append(item)
        else:
            categories[(item.category.name, item.category.weight)] = [item]

    for category_name, category_weight in categories:
        categories_list.append(
            {
                'name': category_name,
                'weight': category_weight,
                'items': categories[(category_name, category_weight)],
            }
        )

    TEMPLATE = "catalog/item_list.html"
    context = {
        "categories_list": categories_list,
    }
    return render(request, TEMPLATE, context)


def item_detail(request, item_num):
    item = get_object_or_404(
        Item.objects.published_items_with_category_name(),
        id=item_num,
    )
    context = {
        "item": item,
    }
    template = "catalog/item_detail.html"
    return render(request, template, context)
