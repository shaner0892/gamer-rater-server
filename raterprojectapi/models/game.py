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
    
    # @property is a decorater, makes a custom property, this is a getter
    @property
    def is_authorized(self):
        return self.__is_authorized
    
    @is_authorized.setter
    def is_authorized(self, value):
        self.__is_authorized = value
        
    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating
        
        # Calculate the average and return it.
        # If you don't know how to calculate average, Google it.
        average = 0 
        if (len(ratings)):
            average = total_rating/len(ratings)
        #return the result
        return average