# Generated by Django 3.2 on 2023-01-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_productsmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='publish',
            field=models.BooleanField(blank=True, default=True, verbose_name='publish'),
        ),
    ]