# Generated by Django 3.2.6 on 2021-08-31 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210831_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]