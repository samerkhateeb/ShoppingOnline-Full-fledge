# Generated by Django 3.2 on 2023-01-19 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_transactionmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactionmodel',
            options={'ordering': ('-sorting', '-id'), 'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions'},
        ),
    ]
