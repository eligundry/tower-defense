from django.db import models

class Tile(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    is_edge = models.BooleanField(default=False)
