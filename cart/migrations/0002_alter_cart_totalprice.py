# Generated by Django 4.1.7 on 2023-04-18 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='totalprice',
            field=models.IntegerField(default=0),
        ),
    ]