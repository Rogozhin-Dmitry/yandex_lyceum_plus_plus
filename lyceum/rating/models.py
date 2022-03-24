from django.db import models
from Core.validators import star_validator
from Core.models import default_model
from django.contrib.auth.models import User
from catalog.models import catalog_item


class rating_rating(default_model, models.Model):
    star = models.PositiveSmallIntegerField(verbose_name='Оценка пользователя',
                                            help_text="от 1 до 5. Соответствие: 1- 'Ненависть', 2 - 'Неприязнь', " +
                                                      "3 - 'Нейтрально', 4 -'Обожание', 5 - 'Любовь'.  Возможно " +
                                                      "нулевое значение.", validators=[star_validator])
    evaluating = models.ForeignKey(User, verbose_name='Оценивающий (пользователь)', on_delete=models.CASCADE)
    evaluated = models.ForeignKey(catalog_item, verbose_name='Оцениваемый (товар)', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = ('evaluating', 'evaluated')

