# Generated by Django 3.2.12 on 2022-03-28 14:07

import Core.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Опублековано"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Только цифры, буквы латиницы и"
                        + " символы - и _",
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                "Enter a valid “slug” consisting of letter"
                                + "s, numbers, underscores or hyphens.",
                                "invalid",
                            )
                        ],
                        verbose_name="Название",
                    ),
                ),
                (
                    "weight",
                    models.PositiveSmallIntegerField(
                        help_text="Больше 0, меньше 32767",
                        verbose_name="Длинна",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Опублековано"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Только цифры, буквы латиницы и "
                        + "символы - и _",
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                "Enter a valid “slug” consisting of lette"
                                + "rs, numbers, underscores or hyphens.",
                                "invalid",
                            )
                        ],
                        verbose_name="Название",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Опублековано"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Макс 150 символов",
                        max_length=150,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="Минимум два слова. Обязательно содер"
                        + "жится слово превосходно или роскошно",
                        validators=[
                            Core.validators.validate_brilliant,
                            Core.validators.count_validator,
                        ],
                        verbose_name="Описание",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        related_name="items", to="catalog.Tag"
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
