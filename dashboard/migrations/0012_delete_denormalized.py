# Generated by Django 4.2.5 on 2023-10-15 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_denormalized_is_weekend'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Denormalized',
        ),
    ]