# Generated by Django 3.2 on 2023-01-19 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20230119_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionmodel',
            name='amount',
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='amount_cost',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='amount_cost'),
        ),
    ]
