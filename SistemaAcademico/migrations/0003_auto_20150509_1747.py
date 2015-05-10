# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaAcademico', '0002_usuario'),
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
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='programa',
            name='codigo',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
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
        migrations.AddField(
            model_name='programa',
            name='facultad',
            field=models.ForeignKey(default='ninguno', to='SistemaAcademico.Facultad'),
            preserve_default=False,
        ),
    ]
