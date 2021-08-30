from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('teams/', views.teams_index, name='teams_index'),
    path('addTeam/', views.TeamCreate.as_view(), name='team_create'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'),
    path('teams/<int:team_id>/', views.teams_detail, name='teams_detail'),
    path('addPlayer/', views.PlayerCreate.as_view(), name='player_create'),
    path('addBaseballPlayer/', views.BaseballPlayerCreate.as_view(), name='baseball_player_create'),
    path('players/<int:player_id>/', views.players_detail, name='players_detail'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
    path('players/', views.players_index, name='players_index'),
    path('baseball/', views.baseball, name='baseball'),
    path('basketball/', views.basketball, name='basketball'),
    path('football/', views.football, name='football'),
    path('hockey/', views.hockey, name='hockey'),
]