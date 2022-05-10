from django.db import models

class Review(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    review = models.CharField(max_length=55)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)