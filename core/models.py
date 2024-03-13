from django.db import models

class World(models.Model):
    people = models.IntegerField()