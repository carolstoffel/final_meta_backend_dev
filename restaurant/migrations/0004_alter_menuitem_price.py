# Generated by Django 5.0 on 2023-12-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_first_name_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(),
        ),
    ]
