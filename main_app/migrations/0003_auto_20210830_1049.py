# Generated by Django 3.2.6 on 2021-08-30 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_auto_20210829_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='baseballPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(choices=[('sp', 'Starter'), ('rp', 'Reliever'), ('1b', 'First Baseman'), ('2b', 'Second Baseman'), ('3b', 'Third Baseman'), ('ss', 'Shortstop'), ('c', 'Catcher'), ('rf', 'Right Fielder'), ('cf', 'Center Fielder'), ('lf', 'Left Fielder'), ('dh', 'Designated Hitter')], default='sp', max_length=25)),
                ('height', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='basketballPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=25)),
                ('height', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='footballPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=25)),
                ('height', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='hockeyPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=25)),
                ('height', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
        migrations.AlterField(
            model_name='team',
            name='sport',
            field=models.CharField(choices=[('baseball', 'Baseball'), ('basketball', 'Basketball'), ('football', 'Football'), ('hockey', 'Hockey')], default='baseball', max_length=20),
        ),
    ]