# Generated by Django 4.2.5 on 2023-10-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denormalized',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(default='', max_length=100)),
                ('is_weekend', models.BooleanField(default=False, verbose_name='is weekend')),
                ('fulfilment', models.CharField(default='', max_length=100)),
                ('saleschannel', models.CharField(default='', max_length=100)),
                ('shipservicelevel', models.CharField(default='', max_length=100)),
                ('courierstatus', models.CharField(default='', max_length=100)),
                ('qty', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('b2b', models.BooleanField(default=False)),
                ('stock', models.IntegerField(default=0)),
                ('shipcity', models.CharField(default='', max_length=100)),
                ('shipstate', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=100)),
                ('size', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
