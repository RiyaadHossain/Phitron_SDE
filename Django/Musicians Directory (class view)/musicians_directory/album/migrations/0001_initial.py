# Generated by Django 5.1.3 on 2024-11-24 06:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.musicianmodel')),
            ],
        ),
    ]
