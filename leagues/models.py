from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True, blank=True)
    flag = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class League(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # League or Cup
    logo = models.URLField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='leagues')

    def __str__(self):
        return self.name

class Season(models.Model):
    year = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    current = models.BooleanField(default=False)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='seasons')

    def __str__(self):
        return f"{self.league.name} - {self.year}"