# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SistemaAcademico.Persona')),
                ('programa', models.ForeignKey(to='SistemaAcademico.Programa')),
            ],
            bases=('SistemaAcademico.persona',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SistemaAcademico.Persona')),
                ('profesion', models.CharField(max_length=2)),
            ],
            bases=('SistemaAcademico.persona',),
        ),
    ]
