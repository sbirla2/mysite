# Generated by Django 3.0.5 on 2020-04-26 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_classes_class_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='class_slug',
            field=models.SlugField(),
        ),
    ]
