# Generated by Django 3.2.9 on 2022-01-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='apellido')),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=30, verbose_name='genero')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
