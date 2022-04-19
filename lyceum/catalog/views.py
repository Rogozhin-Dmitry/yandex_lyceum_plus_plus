from django import forms
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render
from rating.models import Rating

from catalog.models import Item


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('star',)


def item_list(request):
    TEMPLATE = "catalog/item_list.html"
    items = Item.objects.published_items_with_category_name_and_weight()
    context = {
        "item_list": items,
    }
    return render(request, TEMPLATE, context)


def item_detail(request, item_num):
    TEMPLATE = "catalog/item_detail.html"
    item = get_object_or_404(
        Item.objects.published_items_with_category_name(),
        id=item_num,
    )
    rating = Rating.objects.get_rating_form_item_id(item_num).aggregate(
        Avg('star'), Count('star')
    )
    all_ratings = (
        Rating.objects.select_related("item")
        .only('item__id')
        .filter(item__id=item_num)
        .all()
    )
    form = RatingForm(request.POST or None)
    context = {
        "item": item,
        "rating": rating,
        'all_ratings': all_ratings,
        'form': form,
    }
    if request.method == 'POST':
        if form and form.is_valid():
            star = form.cleaned_data['star']
            if not star:
                star = 0
            user = request.user
            Rating.objects.update_or_create(
                user=user,
                item=context['item'],
                defaults={'star': star},
            )
            return redirect('item_detail', item_num=context['item'].pk)
        return render(request, TEMPLATE, context)
    return render(request, TEMPLATE, context)
