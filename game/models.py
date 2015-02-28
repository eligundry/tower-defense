from django.db import models

class Tile(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    is_edge = models.BooleanField(default=False)

    def cell(self):
        return (self.y_coordinate * 10) + x_coordinate

class Tower(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    max_hp = models.IntegerField()
    view_range = models.IntegerField(null=True)
    damage = models.IntegerField(null=True)

class Monster(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    max_hp = models.IntegerField()
    attack_range = models.IntegerField(null=True)
    movement_range = models.IntegerField()
    damage = models.IntegerField()

class Game(models.Model):
    money_earned = models.IntegerField(default=0)
    money_spent = models.IntegerField(default=0)
    enemies_killed = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(null=True)
    tiles = models.ManyToManyField(Tile, through='GameTile')

class GameTile(models.Model):
    game = models.ForeignKey(Game)
    tile = models.ForeignKey(Tile)
    tower = models.ManyToManyField(Tower, through='TileTower',
                                through_fields=('tile', 'tower'), null=True)
    monster = models.ManyToManyField(Monster, through='TileMonster',
                                through_fields=('tile', 'monster'), null=True)

    def is_occupied(self):
        return (self.tower is not null) and (self.monster is not null)

class TileTower(models.Model):
    tile = models.ForeignKey(GameTile)
    tower = models.ForeignKey(Tower)
    hp = models.IntegerField()
    view_range = models.IntegerField()

class TileMonster(models.Model):
    tile = models.ForeignKey(GameTile)
    monster = models.ForeignKey(Monster)
    hp = models.IntegerField()
