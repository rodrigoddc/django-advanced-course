# Generated by Django 3.0.8 on 2020-07-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_slug_populating_empty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
