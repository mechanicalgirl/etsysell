# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_accounts', '0002_auto_20160803_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selleraccount',
            name='market',
            field=models.CharField(choices=[('Etsy', 'Etsy'), ('Artfire', 'ArtFire'), ('Handmadeatamazon', 'Handmade at Amazon'), ('Spoonflower', 'Spoonflower')], default='Etsy', max_length=200),
        ),
        migrations.DeleteModel(
            name='Market',
        ),
    ]