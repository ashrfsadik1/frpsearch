# Generated by Django 3.1 on 2024-04-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20240419_1820'),
        ('display', '0004_auto_20240411_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display_data',
            name='users',
            field=models.ManyToManyField(related_name='display_profile', to='accounts.UserProfile'),
        ),
    ]
