# Generated by Django 3.2.12 on 2022-04-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_auto_20220413_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.CharField(
                blank=True,
                choices=[
                    (1, 'Ненависть'),
                    (2, 'Неприязнь'),
                    (3, 'Нейтрально'),
                    (4, 'Обожание'),
                    (5, 'Любовь'),
                ],
                default=5,
                help_text='Выберите своё отношение к товару',
                max_length=2,
                verbose_name='Оценка',
            ),
        ),
    ]
