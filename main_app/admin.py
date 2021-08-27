from django.contrib import admin

from .models import Position, Team

# Register your models here.

admin.site.register(Team)
admin.site.register(Position)
