# Generated by Django 3.2 on 2023-01-18 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_userprofile_deposite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sorting',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='sorting'),
        ),
    ]
