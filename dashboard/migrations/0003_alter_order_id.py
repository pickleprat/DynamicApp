# Generated by Django 4.2.5 on 2023-10-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order_delete_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='identifier'),
        ),
    ]