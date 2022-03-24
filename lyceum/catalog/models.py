from django.db import models
from Core.validators import validate_brilliant, count_validator
from Core.models import default_model_slug, default_model_is_published, default_model


class catalog_item(default_model, default_model_is_published):
    name = models.CharField(verbose_name='Имя', max_length=150, help_text='Макс 150 символов')
    text = models.TextField(verbose_name='Описание',
                            help_text='Минимум два слова. Обязательно содержится слово превосходно или роскошно',
                            validators=[validate_brilliant, count_validator])
    category = models.ForeignKey('catalog_category', verbose_name='Категория', on_delete=models.CASCADE)
    tegs = models.ManyToManyField('catalog_tag')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.text[:15]


class catalog_tag(default_model, default_model_slug, default_model_is_published):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class catalog_category(default_model, default_model_slug, default_model_is_published):
    weight = models.PositiveSmallIntegerField(verbose_name='Длинна',
                                              help_text='Больше 0, меньше 32767')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
