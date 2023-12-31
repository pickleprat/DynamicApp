# Generated by Django 4.2.5 on 2023-10-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('fulfilment', models.CharField(max_length=100)),
                ('sales_channel', models.CharField(max_length=100)),
                ('ship_service_level', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('courier_status', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('ship_city', models.CharField(max_length=100)),
                ('ship_state', models.CharField(max_length=100)),
                ('b2b', models.BooleanField()),
                ('stock', models.FloatField()),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
