from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SPORT_CHOICES = (
    ('baseball', 'Baseball'),
    ('basketball', 'Basketball'),
    ('football', 'Football'),
    ('hockey', 'Hockey'),
)

POSITION_CHOICES = (
    ('sp', 'Starter'),
    ('rp', 'Reliever'),
    ('1b', 'First Baseman'),
    ('2b', 'Second Baseman'),
    ('3b', 'Third Baseman'),
    ('ss', 'Shortstop'),
    ('catcher', 'Catcher'),
    ('of', 'Outfielder'),
    ('dh', 'Designated Hitter'),
    ('pg', 'Point Guard'),
    ('sg', 'Shooting Guard'),
    ('sf', 'Small Forward'),
    ('pf', 'Power Forward'),
    ('center', 'Center'),
    ('rw', 'Right Winger'),
    ('lw', 'Left Winger'),
    ('d', 'Defender'),
    ('g', 'Goalie'),
    ('qb', 'Quarterback'),
    ('rb', 'Running Back'),
    ('wr', 'Wide Receiver'),
    ('te', 'Tight End'),
    ('ol', 'Offensive Lineman'),
    ('dl', 'Defensive Lineman'),
    ('lb', 'Linebacker'),
    ('cb', 'Cornerback'),
    ('s', 'Safety'),
    ('k', 'Kicker'),
    ('p', 'Punter'),
)




class Team(models.Model):
    city = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='baseball')
    primaryColor = models.CharField(max_length=20)
    secondaryColor = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Player(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='baseball')
    position = models.CharField(max_length=25, choices=POSITION_CHOICES, default='sp')
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)