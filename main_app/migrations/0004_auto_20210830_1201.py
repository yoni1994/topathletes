# Generated by Django 3.2.6 on 2021-08-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210830_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketballplayer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='footballplayer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hockeyplayer',
            name='user',
        ),
        migrations.AddField(
            model_name='player',
            name='sport',
            field=models.CharField(choices=[('baseball', 'Baseball'), ('basketball', 'Basketball'), ('football', 'Football'), ('hockey', 'Hockey')], default='baseball', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('sp', 'Starter'), ('rp', 'Reliever'), ('1b', 'First Baseman'), ('2b', 'Second Baseman'), ('3b', 'Third Baseman'), ('ss', 'Shortstop'), ('catcher', 'Catcher'), ('of', 'Outfielder'), ('dh', 'Designated Hitter'), ('pg', 'Point Guard'), ('sg', 'Shooting Guard'), ('sf', 'Small Forward'), ('pf', 'Power Forward'), ('center', 'Center'), ('rw', 'Right Winger'), ('lw', 'Left Winger'), ('d', 'Defender'), ('g', 'Goalie'), ('qb', 'Quarterback'), ('rb', 'Running Back'), ('wr', 'Wide Receiver'), ('te', 'Tight End'), ('ol', 'Offensive Lineman'), ('dl', 'Defensive Lineman'), ('lb', 'Linebacker'), ('cb', 'Cornerback'), ('s', 'Safety'), ('k', 'Kicker'), ('p', 'Punter')], default='sp', max_length=25),
        ),
        migrations.DeleteModel(
            name='baseballPlayer',
        ),
        migrations.DeleteModel(
            name='basketballPlayer',
        ),
        migrations.DeleteModel(
            name='footballPlayer',
        ),
        migrations.DeleteModel(
            name='hockeyPlayer',
        ),
    ]
