from django.db import models
from leagues.models import Country

class Venue(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    surface = models.CharField(max_length=50, null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    logo = models.URLField()
    code = models.CharField(max_length=10, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    founded = models.IntegerField(null=True, blank=True)
    national = models.BooleanField(default=False)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name