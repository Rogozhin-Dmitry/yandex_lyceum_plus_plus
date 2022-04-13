from random import sample

from Core.constants import NUMBER_DISPLAYED_ITEMS_ON_MAIN_PAGE
from django.db import models
from django.db.models import Prefetch

from catalog.models import Tag


class ItemManager(models.Manager):
    def published_items_ids(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .all()
            .values_list("id", flat=True)
        )

    def published_items(self):
        return (
            self.get_queryset()
            .filter(
                pk__in=sample(
                    list(self.published_items_ids()),
                    NUMBER_DISPLAYED_ITEMS_ON_MAIN_PAGE,
                )
            )
            .prefetch_related(
                Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(is_published=True).only(
                        "name"
                    ),
                )
            )
            .only("name", "text", "tags")
        )
