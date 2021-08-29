# Generated by Django 3.2.4 on 2021-08-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('basket', 'User basket'), ('fixed', 'Fixed by user'), ('completed', 'Completed by warehouse'), ('cancelled', 'Cancelled by warehouse')], default='basket', max_length=20),
        ),
    ]
