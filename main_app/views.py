from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Team, Player
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.




class Home(LoginView):
  template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teams_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def baseball(request):
    teams = Team.objects.filter(user=request.user, sport='baseball')
    players = Player.objects.filter(user=request.user, sport='baseball')
    return render(request, 'baseball.html', { 'teams': teams, 'players': players})

@login_required
def basketball(request):
    teams = Team.objects.filter(user=request.user, sport='basketball')
    return render(request, 'basketball.html', { 'teams': teams })

@login_required
def football(request):
    teams = Team.objects.filter(user=request.user, sport='football')
    return render(request, 'football.html', { 'teams': teams })

@login_required
def hockey(request):
    teams = Team.objects.filter(user=request.user, sport='hockey')
    return render(request, 'hockey.html', { 'teams': teams })

@login_required
def teams_index(request):
    teams = Team.objects.filter(user=request.user)
    return render(request, 'teams/index.html', { 'teams': teams })

@login_required
def players_index(request):
    players = Player.objects.filter(user=request.user)
    return render(request, 'players/index.html', { 'players': players })

class TeamCreate(LoginRequiredMixin, CreateView):
  model = Team
  fields = ['city', 'name', 'sport', 'primaryColor', 'secondaryColor']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/teams'

class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = '__all__'
    success_url = '/teams'

class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = '/teams'

def teams_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  return render(request, 'teams/detail.html', { 'team': team })


class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'sport', 'position', 'height', 'team']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/players'

# class BaseballPlayerCreate(LoginRequiredMixin, CreateView):
#     model = baseballPlayer
#     fields = ['name', 'position', 'height', 'team']
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#     success_url = '/players'

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'
    success_url = '/players'

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players'

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  return render(request, 'players/detail.html', { 'player': player })

# def baseball_players_detail(request, baseballPlayer_id):
#   player = baseballPlayer.objects.get(id=baseballPlayer_id)
#   return render(request, 'players/detail.html', { 'player': player })