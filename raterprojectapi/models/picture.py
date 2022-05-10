from django.db import models

class Picture(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    pictureURL = models.CharField(max_length=500)