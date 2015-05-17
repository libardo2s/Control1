# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaAcademico', '0002_auto_20150510_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
