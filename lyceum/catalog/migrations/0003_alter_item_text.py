# Generated by Django 3.2.12 on 2022-04-11 15:47

import Core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20220407_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(
                help_text=(
                    'Минимум два слова. Обязательно содержится ',
                    'слово превосходно или роскошно',
                ),
                validators=[
                    Core.validators.validate_brilliant,
                    Core.validators.count_validator,
                ],
                verbose_name='Описание',
            ),
        ),
    ]