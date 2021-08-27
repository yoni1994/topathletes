from django.db import models

# Create your models here.
class Team(models.Model):
    city = models.CharField(max_length=25)
    name = models.CharField(max_length=20)
    sport = models.CharField(max_length=20)
    # sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    primaryColor = models.CharField(max_length=20)
    secondaryColor = models.CharField(max_length=20)
    
# teams = [
#     Team('Chicago', 'Cubs', 'baseball', 'blue', 'red'),
#     Team('Chicago', 'Bulls', 'basketball', 'red', 'black'),
#     Team('Chicago', 'Bears', 'football', 'navy', 'orange'),
#     Team('Chicago', 'Blackhawks', 'hockey', 'red', 'black'),
# ]

class Player(models.Model):
    name = models.CharField(max_length=50)
    # sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    position = models.CharField(max_length=25)
    height = models.CharField(max_length=10)
    team = models.CharField(max_length=50)
    
# players = [
#     Player('Ernie Banks', 'baseball', 'shortstop', '6\'1', 'Chicago Cubs'),
#     Player('Derrick Rose', 'basketball', 'point guard', '6\'3', 'Chicago Bulls'),
#     Player('Devin Hester', 'football', 'wide receiver', '5\'11', 'Chicago Bears'),
#     Player('Jonathan Toews', 'hockey', 'center', '6\'2', 'Chicago Blackhawks'),
# ]

class Sport(models.Model):
    name = models.CharField(max_length=10)
    teams = [models.ForeignKey('Team', on_delete=models.CASCADE)]
    positions = [models.ForeignKey('Position', on_delete=models.CASCADE)]


class Position(models.Model):
    name = models.CharField(max_length=20)
    sport = models.CharField(max_length=10)
    # sport = models.ForeignKey('Sport', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
    #     return self.sport
        