from django.db import models
from django.conf import settings
from catalog.models import Item


class Rating(models.Model):
    START_CONST = [
        ('1', 'Ненависть'),
        ('2', 'Неприязнь'),
        ('3', 'Нейтрально'),
        ('4', 'Обожание'),
        ('5', 'Любовь'),
    ]
    star = models.CharField(
        verbose_name='Оценка',
        choices=START_CONST,
        default='5',
        max_length=2,
        help_text="от 1 до 5. Соответствие: 1- 'Ненависть', 2 - 'Неприязнь'," +
                  " 3 - 'Нейтрально', 4 -'Обожание', 5 - 'Любовь'",
        blank=True,
    )
    item = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(Item, verbose_name='Товар',
                             on_delete=models.CASCADE,
                             related_name='rating')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        constraints = [
            models.UniqueConstraint(fields=['item', 'user'],
                                    name='unique_user_item')
        ]

    def __str__(self):
        return self.star
