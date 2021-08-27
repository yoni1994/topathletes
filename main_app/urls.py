from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.teams_index, name='teams_index'),
    path('teams/create/', views.TeamCreate.as_view(), name='team_create'),
    path('addPlayer/', views.PlayerCreate.as_view(), name='player_create'),
    path('players/', views.players_index, name='players_index'),
    path('baseball/', views.baseball, name='baseball'),
    path('basketball/', views.basketball, name='basketball'),
    path('football/', views.football, name='football'),
    path('hockey/', views.hockey, name='hockey'),
]