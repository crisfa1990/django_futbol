from django.db import models
from leagues.models import League, Season
from teams.models import Team

class Standing(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    rank = models.IntegerField()
    points = models.IntegerField()
    goals_diff = models.IntegerField()
    form = models.CharField(max_length=20, null=True, blank=True)

    played = models.IntegerField()
    win = models.IntegerField()
    draw = models.IntegerField()
    lose = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()

    class Meta:
        unique_together = ('team', 'league', 'season')

    def __str__(self):
        return f"{self.team.name} ({self.points} pts)"