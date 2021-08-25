from django.shortcuts import render



# Create your views here.

class Team:
    def __init__(self, city, name, sport, primaryColor, secondaryColor):
        self.city = city
        self.name = name
        self.sport = sport
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
    
teams = [
    Team('Chicago', 'Cubs', 'baseball', 'blue', 'red'),
    Team('Chicago', 'Bulls', 'basketball', 'red', 'black'),
    Team('Chicago', 'Bears', 'football', 'navy', 'orange'),
    Team('Chicago', 'Blackhawks', 'hockey', 'red', 'black'),
]

class Player:
    def __init__(self, name, sport, position, height, team):
        self.name = name
        self.sport = sport
        self.position = position
        self.height = height
        self.team = team
    
players = [
    Player('Ernie Banks', 'baseball', 'shortstop', '6\'1', 'Chicago Cubs'),
    Player('Derrick Rose', 'basketball', 'point guard', '6\'3', 'Chicago Bulls'),
    Player('Devin Hester', 'football', 'wide receiver', '5\'11', 'Chicago Bears'),
    Player('Jonathan Toews', 'hockey', 'center', '6\'2', 'Chicago Blackhawks'),
]


def home(request):
    return render(request, 'home.html')

def baseball(request):
    return render(request, 'baseball.html')

def basketball(request):
    return render(request, 'basketball.html')

def football(request):
    return render(request, 'football.html')

def hockey(request):
    return render(request, 'hockey.html')

def teams_index(request):
    return render(request, 'teams/index.html', { 'teams': teams })

def players_index(request):
    return render(request, 'players/index.html', { 'players': players })