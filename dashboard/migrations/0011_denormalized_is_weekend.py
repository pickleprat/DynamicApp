# Generated by Django 4.2.5 on 2023-10-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_rename_courierstatus_denormalized_courierstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='denormalized',
            name='is_weekend',
            field=models.BooleanField(default=False, verbose_name='is weekend'),
        ),
    ]
