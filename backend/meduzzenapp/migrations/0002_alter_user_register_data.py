# Generated by Django 4.0.4 on 2022-05-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meduzzenapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_data',
            field=models.DateField(auto_now_add=True, verbose_name='register data'),
        ),
    ]