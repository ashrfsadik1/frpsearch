# Generated by Django 3.1 on 2024-04-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20240410_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display_data',
            name='displays',
            field=models.ManyToManyField(related_name='display_data', to='display.Display'),
        ),
    ]
