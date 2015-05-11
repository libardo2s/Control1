# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('materias', models.ManyToManyField(to='SistemaAcademico.Materia')),
            ],
        ),
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
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('facultad', models.ForeignKey(to='SistemaAcademico.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('username', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SistemaAcademico.Persona')),
                ('programa', models.ForeignKey(to='SistemaAcademico.Programa')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('SistemaAcademico.persona',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SistemaAcademico.Persona')),
                ('profesion', models.CharField(max_length=50)),
            ],
            bases=('SistemaAcademico.persona',),
        ),
        migrations.AddField(
            model_name='pensum',
            name='programa',
            field=models.ForeignKey(to='SistemaAcademico.Programa'),
        ),
        migrations.AddField(
            model_name='aula',
            name='bloque',
            field=models.ForeignKey(to='SistemaAcademico.Bloque'),
        ),
    ]
