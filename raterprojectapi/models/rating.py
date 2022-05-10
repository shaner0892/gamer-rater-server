from django.db import models

class Rating(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    rating = models.IntegerField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)