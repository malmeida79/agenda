# Generated by Django 3.0.6 on 2020-05-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200524_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(verbose_name='Data do Evento'),
        ),
    ]
