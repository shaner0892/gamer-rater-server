from django.db import models

class Review(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    review = models.CharField(max_length=55)
    # by adding a related_name=reviews you can access reviews from games and vice versa
    # you don't have to remigrate after adding just a related_name
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")