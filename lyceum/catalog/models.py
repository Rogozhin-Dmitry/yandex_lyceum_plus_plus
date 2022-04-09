from random import sample

from django.db import models
from django.db.models import Prefetch

from Core.constants import NUMBER_DISPLAYED_ITEMS_ON_MAIN_PAGE
from Core.models import IsPublishedMixin, NameMixin, SlugMixin
from Core.validators import count_validator, validate_brilliant


class ItemManager(models.Manager):
    def published_items_ids(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .all()
            .values_list("id", flat=True)
        )

    def published_items_with_tags(self):
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

    def published_items_with_category_name_and_weight(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .select_related("category")
            .only("name", "text", "category__name", 'category__weight')
            .prefetch_related(
                Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(is_published=True).only(
                        "name"
                    ),
                )
            )
        )

    def published_items_with_category_name(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .select_related("category")
            .only("name", "text", "category__name", 'category__weight')
            .prefetch_related(
                Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(is_published=True).only(
                        "name"
                    ),
                )
            )
        )


class Item(IsPublishedMixin, NameMixin):
    text = models.TextField(
        verbose_name="Описание",
        help_text=(
            "Минимум два слова. Обязательно содержится ",
            "слово превосходно или роскошно",
        ),
        validators=[validate_brilliant, count_validator],
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        on_delete=models.CASCADE,
        related_name="items",
    )
    tags = models.ManyToManyField("Tag", related_name="items")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]

    objects = ItemManager()


class Tag(SlugMixin, IsPublishedMixin, NameMixin):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(SlugMixin, IsPublishedMixin, NameMixin):
    weight = models.PositiveSmallIntegerField(
        verbose_name="Длинна", help_text="Больше 0, меньше " + "32767"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
