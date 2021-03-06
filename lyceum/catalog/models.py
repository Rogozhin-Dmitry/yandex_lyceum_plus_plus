from random import sample

from django.db import models
from django.db.models import Prefetch
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail, ImageField

from Core.constants import NUMBER_DISPLAYED_ITEMS_ON_MAIN_PAGE
from Core.models import IsPublishedMixin, NameMixin, SlugMixin
from Core.validators import count_validator, validate_brilliant


class ItemManager(models.Manager):
    def published_items_ids(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .select_related("category")
            .only(
                "name",
                "text",
                "category__name",
                'category__weight',
                'category__is_published',
            )
            .filter(category__is_published=True)
            .prefetch_related(
                Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(is_published=True).only('id'),
                )
            )
            .all()
            .values_list("id", flat=True)
        )

    def published_items_with_tags(self):
        published_items_ids_list = list(self.published_items_ids())
        if len(published_items_ids_list) >= 3:
            items_id = sample(
                list(self.published_items_ids()),
                NUMBER_DISPLAYED_ITEMS_ON_MAIN_PAGE,
            )
        else:
            items_id = published_items_ids_list

        return (
            self.get_queryset()
            .filter(pk__in=items_id)
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
            .only(
                "name",
                "text",
                "category__name",
                'category__weight',
                'category__is_published',
            )
            .filter(category__is_published=True)
            .order_by('category__weight')
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
            .only("name", "text", "category__name", "category__is_published")
            .filter(category__is_published=True)
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
        verbose_name="????????????????",
        help_text=(
            "?????????????? ?????? ??????????. ?????????????????????? ???????????????????? ",
            "?????????? ?????????????????????? ?????? ????????????????",
        ),
        validators=[validate_brilliant, count_validator],
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="??????????????????",
        on_delete=models.CASCADE,
        related_name="items",
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name="items",
        verbose_name="????????",
    )

    main_image = ImageField(
        verbose_name="???????????????? ????????????????",
        help_text="?????????? ????????????????, ?????? ???? ???? ?????? ????????????????...",
        upload_to='uploads/',
        default='',
    )

    images = models.ManyToManyField(
        'ImageModel',
        verbose_name="????????????????",
    )

    def get_image_1000x650(self):
        if self.main_image:
            return get_thumbnail(self.main_image, '1000x650', quality=51)
        return {"url": 'standard'}

    def get_image_300x255(self):
        if self.main_image:
            return get_thumbnail(self.main_image, '300x255', quality=51)
        return {"url": 'standard'}

    def small_text(self):
        if len(str(self.text)) > 101:
            return str(self.text)[:100]
        return str(self.text)

    small_text.short_description = '????????????????'

    def admin_image(self):
        if self.main_image:
            return format_html(
                f'<img src="{self.main_image.url}" '
                + 'style="width: 45px; height:45px;" />'
            )
        return '?????? ??????????????????????'

    admin_image.allow_tags = True
    admin_image.short_description = '???????????????? ????????????????'

    class Meta:
        verbose_name = "??????????"
        verbose_name_plural = "????????????"

    objects = ItemManager()


class ImageModel(NameMixin):
    img = ImageField(
        verbose_name="????????????????",
        help_text="???????????????? ????????????",
        upload_to='uploads/',
    )

    def get_image_1000x650(self):
        return get_thumbnail(self.img, '1000x650', quality=51)

    def img_preview(self):
        if self.img:
            return format_html(
                f'<img src="{self.img.url}" '
                + 'style="width: 45px; height:45px;" />',
            )
        return '?????? ??????????????????????'

    img_preview.allow_tags = True
    img_preview.short_description = '???????????????? ????????????????'

    class Meta:
        verbose_name = "????????????????"
        verbose_name_plural = "????????????????"


class Tag(SlugMixin, IsPublishedMixin, NameMixin):
    class Meta:
        verbose_name = "??????"
        verbose_name_plural = "????????"


class Category(SlugMixin, IsPublishedMixin, NameMixin):
    weight = models.PositiveSmallIntegerField(
        verbose_name="????????????", help_text="???????????? 0, ???????????? " + "32767"
    )

    class Meta:
        verbose_name = "??????????????????"
        verbose_name_plural = "??????????????????"
