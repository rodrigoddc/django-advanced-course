# Generated by Django 3.0.8 on 2020-07-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]