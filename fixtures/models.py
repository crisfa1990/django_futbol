from django.db import models
from leagues.models import League, Season
from teams.models import Team, Venue

class Fixture(models.Model):
    api_id = models.IntegerField(unique=True)
    date = models.DateTimeField()
    status_long = models.CharField(max_length=50)
    status_short = models.CharField(max_length=10)
    elapsed = models.IntegerField(null=True, blank=True)
    referee = models.CharField(max_length=100, null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True)

    goals_home = models.IntegerField(null=True, blank=True)
    goals_away = models.IntegerField(null=True, blank=True)

    score_ht_home = models.IntegerField(null=True, blank=True)
    score_ht_away = models.IntegerField(null=True, blank=True)
    score_ft_home = models.IntegerField(null=True, blank=True)
    score_ft_away = models.IntegerField(null=True, blank=True)

    round = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date.strftime('%Y-%m-%d')}"