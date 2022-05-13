"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game
from raterprojectapi.models.player import Player
from raterprojectapi.models.review import Review

class GameView(ViewSet):
    """Gamer rater game types view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        
        Returns:
            Response -- JSON serialized game type
        """
        game = Game.objects.get(pk=pk)
        player = Player.objects.get(user=request.auth.user)
        game.is_authorized = game.player == player
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET requests to get all game types
        
        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        game = Game.objects.get(pk=serializer.data["id"])
        # *request.data["categories"] grabs the array of categories, but * breaks it into single arguments
        game.categories.add(*request.data["categories"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ['id', 'title', 'designer', 'description', 'year_released', 'number_of_players', 
                'estimated_time_to_play', 'age_recommendation', 'player', 'categories', 'reviews', 'is_authorized']
        depth = 1
        
class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # you don't need to add categories because it's not a required field
        fields = ['id', 'title', 'designer', 'description', 'year_released', 'number_of_players', 
                'estimated_time_to_play', 'age_recommendation']