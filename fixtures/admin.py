from django.contrib import admin
from .models import Fixture

@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'home_team', 'away_team',
        'goals_home', 'goals_away',
        'league', 'season', 'status_short'
    )
    list_filter = ('league', 'season', 'status_short')
    search_fields = ('home_team__name', 'away_team__name')
    ordering = ('-date',)