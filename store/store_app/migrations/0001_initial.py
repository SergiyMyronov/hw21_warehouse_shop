# Generated by Django 3.2.4 on 2021-08-29 11:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('author_name', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pubdate', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(unique=True)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('store_num', models.IntegerField()),
                ('store_name', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_mail', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('basket', 'User basket'), ('fixed', 'Fixed by user'), ('completed', 'Completed by warehouse')], default='basket', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('store_num', models.IntegerField()),
                ('last_update_date', models.DateField(default=datetime.datetime(1901, 1, 1, 0, 0))),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('author_name', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.order')),
            ],
        ),
    ]
