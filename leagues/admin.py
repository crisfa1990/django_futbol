from django.contrib import admin
from .models import Country, League, Season

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'country', 'api_id')
    list_filter = ('type', 'country')
    search_fields = ('name',)

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('league', 'year', 'start', 'end', 'current')
    list_filter = ('league', 'current')