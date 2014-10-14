# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0002_list_list_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='current_location',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
