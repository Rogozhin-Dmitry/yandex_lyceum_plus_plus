from django import forms
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from catalog.models import Item
from rating.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('star',)


class ItemList(TemplateView):
    TEMPLATE = "catalog/item_list.html"

    def get(self, request, *args, **kwargs):
        items = Item.objects.published_items_with_category_name_and_weight()
        context = {
            "item_list": items,
        }
        return render(request, self.TEMPLATE, context)


class ItemDetail(TemplateView):
    TEMPLATE = "catalog/item_detail.html"

    @staticmethod
    def get_context(item_num, form):
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
        return {
            "item": item,
            "rating": rating,
            'all_ratings': all_ratings,
            'form': form,
        }

    def post(self, request, item_num):
        form = RatingForm(request.POST or None)
        context = self.get_context(item_num, form)
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
            return render(request, self.TEMPLATE, context)

    def get(self, request, item_num='0', *args, **kwargs):
        form = RatingForm(request.POST or None)
        context = self.get_context(item_num, form)
        return render(request, self.TEMPLATE, context)
