from django.contrib import admin
from rating.models import rating_rating


@admin.register(rating_rating)
class RatingRatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'evaluating', 'evaluated')