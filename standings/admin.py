from django.contrib import admin
from .models import Standing

@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = (
        'team', 'league', 'season', 'rank', 'points',
        'played', 'win', 'draw', 'lose', 'goals_for', 'goals_against'
    )
    list_filter = ('league', 'season')
    search_fields = ('team__name',)