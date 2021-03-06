"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models.player import Player
from raterprojectapi.models.review import Review

class GameReviewView(ViewSet):
    """Gamer rater game types view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        
        Returns:
            Response -- JSON serialized game type
        """
        review = Review.objects.get(pk=pk)
        serializer = GameReviewSerializer(review)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET requests to get all game types
        
        Returns:
            Response -- JSON serialized list of game types
        """
        reviews = Review.objects.all()
        serializer = GameReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateGameReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class GameReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Review
        fields = ['id', 'player', 'review', 'game']
        depth = 1
        
class CreateGameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review', 'game']