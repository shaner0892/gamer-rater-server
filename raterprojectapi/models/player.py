from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    # on_delete=models.CASCADE if you delete this user, it will delete any data related to that user
    # user is a one to one because one user can only be one gamer; otherwise it would be foreign key 
    # because a user could have multiple games, events, etc
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)