from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SPORT_CHOICES = (
    ('baseball', 'Baseball'),
    ('basketball', 'Basketball'),
    ('football', 'Football'),
    ('hockey', 'Hockey'),
)

BASEBALL_CHOICES = (
    ('sp', 'Starter'),
    ('rp', 'Reliever'),
    ('1b', 'First Baseman'),
    ('2b', 'Second Baseman'),
    ('3b', 'Third Baseman'),
    ('ss', 'Shortstop'),
    ('c', 'Catcher'),
    ('rf', 'Right Fielder'),
    ('cf', 'Center Fielder'),
    ('lf', 'Left Fielder'),
    ('dh', 'Designated Hitter'),
)




class Team(models.Model):
    city = models.CharField(max_length=25)
    name = models.CharField(max_length=20)
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='baseball')
    primaryColor = models.CharField(max_length=20)
    secondaryColor = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Player(models.Model):
    name = models.CharField(max_length=50)
    # sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='baseball')
    position = models.CharField(
        max_length=25,
        # if sport == 'baseball':
        #     choices=BASEBALL_CHOICES
        # elif sport == 'basketball':
        #     choices=BASKETBALL_CHOICES
        # elif sport == 'basketball':
        #     choices=BASKETBALL_CHOICES
        # else:
        #     choices=BASKETBALL_CHOICES
        )
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class baseballPlayer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=25, choices=BASEBALL_CHOICES, default='sp')
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class basketballPlayer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=25)
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class footballPlayer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=25)
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class hockeyPlayer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=25)
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

# class Sport(models.Model):
#     name = models.CharField(max_length=10)
#     teams = [models.ForeignKey('Team', on_delete=models.CASCADE)]
#     positions = [models.ForeignKey('Position', on_delete=models.CASCADE)]


# class Position(models.Model):
#     name = models.CharField(max_length=20)
#     sport = models.CharField(max_length=10)
    # sport = models.ForeignKey('Sport', on_delete=models.CASCADE)

        