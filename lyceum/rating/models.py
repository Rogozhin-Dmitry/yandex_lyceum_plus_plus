from django.conf import settings
from django.db import models

from catalog.models import Item


class RatingManager(models.Manager):
    def get_rating_form_item_id(self, item_id):
        return (
            self.get_queryset()
            .select_related("item")
            .only('item__id')
            .filter(item__id=item_id)
            .all()
            .values_list("star", flat=True)
        )


class Rating(models.Model):
    START_CONST = [
        (1, "Ненависть"),
        (2, "Неприязнь"),
        (3, "Нейтрально"),
        (4, "Обожание"),
        (5, "Любовь"),
    ]
    star = models.IntegerField(
        verbose_name="Оценка",
        choices=START_CONST,
        default=5,
        help_text="Выберите своё отношение к товару",
        blank=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="rating",
    )
    item = models.ForeignKey(
        Item,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="rating",
    )

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
        constraints = [
            models.UniqueConstraint(
                fields=["item", "user"], name="unique_user_item"
            )
        ]

    def __str__(self):
        return self.star

    objects = RatingManager()
