from django.db import models

class player(models.Model):
    player = models.CharField(max_length=10)
    Hp = models.IntegerField(default=100)
    Mp = models.IntegerField(default=1)
    Charactercard = models.IntegerField(default=0)
    Activecard1 = models.IntegerField(default=0)
    Activecard2 = models.IntegerField(default=0)
    Activecard3 = models.IntegerField(default=0)
    party_number = models.IntegerField(default=0)