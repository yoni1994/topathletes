from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    city = models.CharField(max_length=25)
    name = models.CharField(max_length=20)
    sport = models.CharField(max_length=20)
    # sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    primaryColor = models.CharField(max_length=20)
    secondaryColor = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Player(models.Model):
    name = models.CharField(max_length=50)
    # sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    position = models.CharField(max_length=25)
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Sport(models.Model):
    name = models.CharField(max_length=10)
    teams = [models.ForeignKey('Team', on_delete=models.CASCADE)]
    positions = [models.ForeignKey('Position', on_delete=models.CASCADE)]


class Position(models.Model):
    name = models.CharField(max_length=20)
    sport = models.CharField(max_length=10)
    # sport = models.ForeignKey('Sport', on_delete=models.CASCADE)

        