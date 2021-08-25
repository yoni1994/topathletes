from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('baseball/', views.baseball, name='baseball'),
    path('basketball/', views.basketball, name='basketball'),
    path('football/', views.football, name='football'),
    path('hockey/', views.hockey, name='hockey'),
]