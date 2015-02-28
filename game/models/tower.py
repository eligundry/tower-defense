from django.db import models

class Tower(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField()
    attack_range = models.IntegerField()
    damage = models.IntegerField(null=True)
