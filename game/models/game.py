from django.db import models
from .tile import Tile

class Game(models.Model):
    money_earned = models.IntegerField(default=0)
    money_spent = models.IntegerField(default=0)
    enemies_killed = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(null=True)
    tiles = models.ManyToManyField(Tile, through='GameTile')

class GameTile(models.Model):
    game = models.ForeignKey(Game)
    tile = models.ForeignKey(Tile)
