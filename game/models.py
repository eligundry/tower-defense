from django.db import models

class Tile(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    is_edge = models.BooleanField(default=False)

class Tower(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField()
    attack_range = models.IntegerField()
    damage = models.IntegerField(null=True)

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
    tower = models.ManyToManyField(Tower, through='TileTower',
                                   through_fields=('tile', 'tower'))

class TileTower(models.Model):
    tile = models.ForeignKey(GameTile)
    tower = models.ForeignKey(Tower)
