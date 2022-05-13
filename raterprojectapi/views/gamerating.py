"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models.player import Player
from raterprojectapi.models.rating import Rating

class GameRatingView(ViewSet):
    """Gamer rater game types view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        
        Returns:
            Response -- JSON serialized game type
        """
        rating = Rating.objects.get(pk=pk)
        serializer = GameRatingSerializer(rating)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET requests to get all game types
        
        Returns:
            Response -- JSON serialized list of game types
        """
        ratings = Rating.objects.all()
        serializer = GameRatingSerializer(ratings, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateGameRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class GameRatingSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Rating
        fields = ['id', 'player', 'rating', 'game']
        depth = 1
        
class CreateGameRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'game']