# Generated by Django 2.1.5 on 2019-02-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='special_vehicle_info',
            field=models.CharField(blank=True, choices=[('p', 'pets friendly'), ('s', 'smoke free'), ('w', 'wheelchair'), ('b', 'provide beverage')], max_length=20),
        ),
    ]
