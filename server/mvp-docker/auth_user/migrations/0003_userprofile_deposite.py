# Generated by Django 3.2 on 2023-01-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0002_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='deposite',
            field=models.CharField(blank=True, choices=[('5', '5'), ('10', '10'), ('50', '50'), ('100', '100')], default='5', max_length=10, null=True, verbose_name='deposite'),
        ),
    ]
