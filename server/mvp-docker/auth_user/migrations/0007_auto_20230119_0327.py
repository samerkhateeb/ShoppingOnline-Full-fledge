# Generated by Django 3.2 on 2023-01-19 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0006_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='deposite',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='amountp',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='amountp'),
        ),
    ]