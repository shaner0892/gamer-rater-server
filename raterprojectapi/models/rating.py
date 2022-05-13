from django.db import models

class Rating(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    rating = models.IntegerField()
    # adding related_name: allows you to access the list of all rating associated with
    # an individual game on the game side of the relationship using the related name.
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")