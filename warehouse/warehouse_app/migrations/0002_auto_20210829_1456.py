# Generated by Django 3.2.4 on 2021-08-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='order_num',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='update_date',
            field=models.DateField(blank=True),
        ),
    ]
