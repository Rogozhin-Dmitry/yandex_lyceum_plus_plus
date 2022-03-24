from django.db import models
from django.core.validators import validate_slug


class default_model(models.Model):
    id = models.AutoField(verbose_name='ИД', primary_key=True)

    class Meta:
        abstract = True


class default_model_is_published(models.Model):
    is_published = models.BooleanField(verbose_name='Опублековано', default=True)

    class Meta:
        abstract = True


class default_model_slug(models.Model):
    slug = models.SlugField(verbose_name='Название',
                            help_text='Только цифры, буквы латиницы и символы - и _',
                            validators=[validate_slug], max_length=200, unique=True)

    class Meta:
        abstract = True
