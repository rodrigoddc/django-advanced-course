# Generated by Django 3.0.8 on 2020-07-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0006_auto_20200715_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='vimeo_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]