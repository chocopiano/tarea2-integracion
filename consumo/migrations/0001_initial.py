# Generated by Django 3.0.5 on 2020-04-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hamburguesa',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('idi', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
