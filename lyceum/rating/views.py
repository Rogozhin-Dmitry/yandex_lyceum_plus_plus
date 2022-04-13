from django import forms
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from rating.models import Rating

from catalog.models import Item


class NewRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('star',)


def new_rating_form(request, item_num):
    TEMPLATE = "rating/new_rating_form.html"
    if not request.user.is_authenticated:
        return HttpResponseNotFound()
    item = get_object_or_404(
        Item.objects.published_items_with_category_name(),
        id=item_num,
    )
    form = NewRatingForm(request.POST or None)
    if form.is_valid():
        star = form.cleaned_data['star']
        user = request.user
        rating = Rating.objects.get_rating_form_user_id_and_item_id(
            request.user.id, item.id
        )
        if rating:
            rating.star = star
            rating.save(update_fields=['star'])
        else:
            Rating.objects.create(
                star=star,
                user=user,
                item=item,
            )
        return redirect(f'/catalog/{item.pk}')

    context = {
        "item": item,
        "form": form,
    }
    return render(request, TEMPLATE, context)
