from django.db import models
from django.core.validators import validate_slug


class IsPublishedMixin(models.Model):
    is_published = models.BooleanField(verbose_name='Опублековано',
                                       default=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(verbose_name='Название',
                            help_text='Только цифры, буквы латиницы и си' +
                                      'мволы - и _',
                            validators=[validate_slug], max_length=200,
                            unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug[:15]
