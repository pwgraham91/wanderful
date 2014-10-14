# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0004_auto_20140919_0304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='city',
            new_name='city_state',
        ),
        migrations.RemoveField(
            model_name='location',
            name='state',
        ),
    ]
