# Generated by Django 2.0.2 on 2019-06-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='Latitud',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='registro',
            name='Longitud',
            field=models.CharField(max_length=200),
        ),
    ]
