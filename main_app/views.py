from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Team, Player
from django.contrib.auth.views import LoginView


# Create your views here.




class Home(LoginView):
  template_name = 'home.html'

def baseball(request):
    return render(request, 'baseball.html')

def basketball(request):
    return render(request, 'basketball.html')

def football(request):
    return render(request, 'football.html')

def hockey(request):
    return render(request, 'hockey.html')

def teams_index(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', { 'teams': teams })

def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', { 'players': players })

class TeamCreate(CreateView):
  model = Team
  fields = ['city', 'name', 'sport', 'primaryColor', 'secondaryColor']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/teams'

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'
    success_url = '/teams'

class TeamDelete(DeleteView):
    model = Team
    success_url = '/teams'

def teams_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  return render(request, 'teams/detail.html', { 'team': team })


class PlayerCreate(CreateView):
    model = Player
    fields = ['name', 'position', 'height', 'team']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/players'

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'
    success_url = '/players'

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  return render(request, 'players/detail.html', { 'player': player })