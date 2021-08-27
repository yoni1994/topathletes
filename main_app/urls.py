from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.teams_index, name='teams_index'),
    path('addTeam/', views.TeamCreate.as_view(), name='team_create'),
    path('teams/<int:team_id>/', views.teams_detail, name='teams_detail'),
    path('addPlayer/', views.PlayerCreate.as_view(), name='player_create'),
    path('players/<int:player_id>/', views.players_detail, name='players_detail'),
    path('players/', views.players_index, name='players_index'),
    path('baseball/', views.baseball, name='baseball'),
    path('basketball/', views.basketball, name='basketball'),
    path('football/', views.football, name='football'),
    path('hockey/', views.hockey, name='hockey'),
]