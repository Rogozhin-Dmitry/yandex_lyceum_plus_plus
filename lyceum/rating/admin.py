from django.contrib import admin
from rating.models import Rating


@admin.register(Rating)
class RatingRatingAdmin(admin.ModelAdmin):
    list_display = ("star", "item", "user")
