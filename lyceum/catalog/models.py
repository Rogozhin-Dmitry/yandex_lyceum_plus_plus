from django.db import models
from Core.validators import validate_brilliant, count_validator
from Core.models import SlugMixin, IsPublishedMixin


class Item(IsPublishedMixin):
    name = models.CharField(verbose_name='Имя', max_length=150,
                            help_text='Макс 150 символов')
    text = models.TextField(verbose_name='Описание',
                            help_text='Минимум два слова. Обязательно содерж' +
                                      'ится слово превосходно или роскошно',
                            validators=[validate_brilliant, count_validator])
    category = models.ForeignKey('Category', verbose_name='Категория',
                                 on_delete=models.CASCADE,
                                 related_name='items')
    tags = models.ManyToManyField('Tag', related_name='items')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.text[:15]


class Tag(SlugMixin, IsPublishedMixin):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(SlugMixin, IsPublishedMixin):
    weight = models.PositiveSmallIntegerField(verbose_name='Длинна',
                                              help_text='Больше 0, меньше ' +
                                                        '32767')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
