from django.db import models
from random import randint

class GameManager(models.Manager):
    def create_game(self, width=10, height=10):
        game = self.create(width=width, height=height)
        return game

class Game(models.Model):
    money_earned = models.IntegerField(default=0)
    money_spent = models.IntegerField(default=0)
    enemies_killed = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(null=True)
    tiles = models.ManyToManyField('Tile', through='GameTile')

    objects = GameManager()

    def end(self):
        from datetime import datetime
        self.is_active = False
        self.time_end = datetime.now()
        self.save()

    def spawn_enemies(self):
        enemy_count = randint(1, 15)
        edge_tiles = self.tiles.filter(is_edge=True)
        monsters = Monster.objects.all()

        for i in range(0, enemy_count):
            tile = edge_tiles[randint(0, edge_tiles.count() - 1)]
            gametile = tile.gametile_set.first()
            monster = monsters[randint(0, monsters.count() - 1)]
            tm = TileMonster(tile=gametile, monster=monster, hp=monster.max_hp)
            tm.save()

    def move_enemies(self):
        monster_tiles = self.gametile_set.exclude(monster__isnull=True)
        tower_tiles = self.gametile_set.exclude(tower__isnull=True)

    def add_tiles(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                tile = Tile()
                tile.y_coordinate = y
                tile.x_coordinate = x

                if (y == 0 or y == self.height - 1):
                    tile.is_edge = True
                elif (x == 0 or x == self.height - 1):
                    tile.is_edge = True

                tile.save()
                game_tile = GameTile.objects.create(game=self, tile=tile)

        # Add the castle on init
        castle = Tower.objects.get(pk=1)
        gt = self.tiles \
                 .filter(x_coordinate=((self.width - 1) / 2)) \
                 .get(y_coordinate=((self.width - 1) / 2)) \
                 .gametile_set.get()

        tt = TileTower.objects.create(tile=gt, tower=castle, hp=castle.max_hp,
                                      view_range=castle.view_range)
        tt.save()

class GameTile(models.Model):
    game = models.ForeignKey('Game')
    tile = models.ForeignKey('Tile')
    tower = models.ManyToManyField('Tower', through='TileTower',
                                through_fields=('tile', 'tower'), null=True)
    monster = models.ManyToManyField('Monster', through='TileMonster',
                                through_fields=('tile', 'monster'), null=True)

    def is_occupied(self):
        return (self.tower is not None) and (self.monster is not None)

class Tile(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    is_edge = models.BooleanField(default=False)

    def cell(self):
        return (self.y_coordinate * 10) + self.x_coordinate

    def coordinates(self):
        return [self.x_coordinate, self.y_coordinate]

    class Meta:
        ordering = ['y_coordinate', 'x_coordinate']

class Monster(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    max_hp = models.IntegerField()
    attack_range = models.IntegerField(null=True)
    movement_range = models.IntegerField()
    damage = models.IntegerField()

class TileMonster(models.Model):
    tile = models.ForeignKey('GameTile')
    monster = models.ForeignKey('Monster')
    hp = models.IntegerField()

class Tower(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    max_hp = models.IntegerField()
    view_range = models.IntegerField(null=True)
    damage = models.IntegerField(null=True)

class TileTower(models.Model):
    tile = models.ForeignKey('GameTile')
    tower = models.ForeignKey('Tower')
    hp = models.IntegerField()
    view_range = models.IntegerField()
