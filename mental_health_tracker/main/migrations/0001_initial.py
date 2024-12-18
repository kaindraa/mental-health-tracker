# Generated by Django 5.1.1 on 2024-10-22 13:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('kategori', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('kategori', models.CharField(max_length=255)),
                ('harga', models.IntegerField()),
                ('diskon', models.IntegerField()),
                ('deskripsi', models.TextField()),
                ('restoran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.restaurant')),
            ],
        ),
    ]
