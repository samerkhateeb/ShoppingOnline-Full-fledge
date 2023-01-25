# Generated by Django 3.2 on 2023-01-19 03:27

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('products', '0013_auto_20230119_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_image', to=settings.FILER_IMAGE_MODEL, verbose_name='image'),
        ),
    ]