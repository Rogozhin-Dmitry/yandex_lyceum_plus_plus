from django.shortcuts import get_object_or_404, render
from rating.models import Rating

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
    all_ratings = list(Rating.objects.get_rating_form_item_id(item_num))
    if all_ratings:
        rating = {'stars': sum(all_ratings), 'count': len(all_ratings)}
    else:
        rating = {'stars': 0, 'count': 0}
    if request.user.is_authenticated:
        user_rating = Rating.objects.get_rating_form_user_id_and_item_id(
            request.user.id, item.id
        )
        if user_rating:
            user_rating = user_rating.star
    else:
        user_rating = 0
    context = {"item": item, "rating": rating, 'user_rating': user_rating}
    TEMPLATE = "catalog/item_detail.html"
    return render(request, TEMPLATE, context)


def estimate_item(request, item_num):
    return '<h1>Страница ещё в разработке</h1>'
