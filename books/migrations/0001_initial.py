# Generated by Django 2.2.24 on 2021-08-01 15:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=20)),
                ('surname_author', models.CharField(max_length=40)),
                ('year_of_birth_autor', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(-2100)])),
            ],
        ),
    ]