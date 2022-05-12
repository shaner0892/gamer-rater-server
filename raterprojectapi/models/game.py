from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="games")