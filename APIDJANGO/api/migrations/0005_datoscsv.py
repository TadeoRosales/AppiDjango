# Generated by Django 3.2.4 on 2023-10-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20231023_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datoscsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.CharField(max_length=100)),
                ('Nombre', models.CharField(max_length=100)),
                ('pregunta1', models.CharField(max_length=100)),
                ('Pregunta2', models.CharField(max_length=100)),
                ('Pregunta3', models.CharField(max_length=100)),
                ('Pregunta4', models.CharField(max_length=100)),
                ('Pregunta5', models.CharField(max_length=100)),
                ('Pregunta6', models.CharField(max_length=100)),
                ('Pregunta7', models.CharField(max_length=100)),
                ('Pregunta8', models.CharField(max_length=100)),
                ('Pregunta9', models.CharField(max_length=100)),
                ('Pregunta10', models.CharField(max_length=100)),
            ],
        ),
    ]