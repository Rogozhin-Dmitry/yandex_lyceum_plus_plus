from django.shortcuts import get_object_or_404, render

# from rating.models import Rating

from catalog.models import Item


def item_list(request):
    TEMPLATE = "catalog/item_list.html"
    items = Item.objects.published_items_with_category_name_and_weight()
    context = {
        "item_list": items,
    }
    return render(request, TEMPLATE, context)


def item_detail(request, item_num):
    item = get_object_or_404(
        Item.objects.published_items_with_category_name(),
        id=item_num,
    )
    # all_ratings = map(int, Rating.objects.get_rating_form_item_id(item_num))
    # if all_ratings:
    #     rating = {'stars': sum(all_ratings), 'count': 8}
    # else:
    #     rating = {'stars': 0, 'count': 0}
    rating = {'stars': 0, 'count': 0}
    context = {"item": item, "rating": rating}
    template = "catalog/item_detail.html"
    return render(request, template, context)


def estimate_item(request, item_num):
    return '<h1>Страница ещё в разработке</h1>'
