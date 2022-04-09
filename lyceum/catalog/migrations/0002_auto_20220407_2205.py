# Generated by Django 3.2.12 on 2022-04-07 19:05

import re

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="name",
            field=models.CharField(
                default=None,
                help_text="Макс 150 символов",
                max_length=150,
                verbose_name="Имя",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tag",
            name="name",
            field=models.CharField(
                default=None,
                help_text="Макс 150 символов",
                max_length=150,
                verbose_name="Имя",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                help_text="Только цифры, буквы латиницы и символы - и _",
                max_length=200,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^[-a-zA-Z0-9_]+\\Z"),
                        "Enter a valid “slug” consisting of letters,"
                        + " numbers, underscores or hyphens.",
                        "invalid",
                    )
                ],
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(
                help_text="Только цифры, буквы латиницы и символы - и _",
                max_length=200,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^[-a-zA-Z0-9_]+\\Z"),
                        "Enter a valid “slug” consisting of letters,"
                        + " numbers, underscores or hyphens.",
                        "invalid",
                    )
                ],
                verbose_name="Описание",
            ),
        ),
    ]