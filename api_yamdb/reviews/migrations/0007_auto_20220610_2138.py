# Generated by Django 2.2.16 on 2022-06-10 21:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220610_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=0, help_text='Введдите оценку', validators=[django.core.validators.MaxValueValidator(10, message='Максимальная оценка'), django.core.validators.MinValueValidator(1, message='Минимальная оценка')], verbose_name='Оценка'),
        ),
    ]
