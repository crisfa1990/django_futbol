from django.contrib import admin
from .models import Team, Venue

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country', 'founded', 'national')
    list_filter = ('country', 'national')
    search_fields = ('name', 'code')

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'capacity', 'surface')
    search_fields = ('name', 'city')