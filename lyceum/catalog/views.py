from django import forms
from django.db.models import Avg, Count
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
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


class ItemDetail(View):
    TEMPLATE = "catalog/item_detail.html"

    def standard(self, request, item_num):
        item = get_object_or_404(
            Item.objects.published_items_with_category_name(),
            id=item_num,
        )
        rating = Rating.objects.get_rating_form_item_id(item_num).aggregate(
            Avg('star'), Count('star')
        )
        if request.user.is_authenticated:
            user_rating = Rating.objects.get_rating_form_user_id_and_item_id(
                request.user.id, item.id
            )
            if user_rating:
                user_rating = user_rating.star
        else:
            user_rating = 0
        form = RatingForm(request.POST or None)
        return {
            "item": item,
            "rating": rating,
            'user_rating': user_rating,
            'form': form,
        }

    def get(self, request, item_num):
        context = self.standard(request, item_num)
        return render(request, self.TEMPLATE, context)

    def post(self, request, item_num):
        if not request.user.is_authenticated:
            return HttpResponseNotFound()
        context = self.standard(request, item_num)
        form = context['form']
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
        return render(request, self.TEMPLATE, context)
