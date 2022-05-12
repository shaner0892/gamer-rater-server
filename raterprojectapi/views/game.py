"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game
from raterprojectapi.models import Category
from raterprojectapi.models.player import Player
from raterprojectapi.views import game_categories

class GameView(ViewSet):
    """Gamer rater game types view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        
        Returns:
            Response -- JSON serialized game type
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET requests to get all game types
        
        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        # for game in games:
        #     found_categories = Category.objects.filter(gamecategory__game = game)
        #     categories = []
        #     for category in found_categories:
        #         game.categories.append(category.__dict__)
        #     game.categories = categories
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
                'estimated_time_to_play', 'age_recommendation', 'player', 'categories']
        depth = 1
        
class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # you don't need to add categories because it's not a required field
        fields = ['id', 'title', 'designer', 'description', 'year_released', 'number_of_players', 
                'estimated_time_to_play', 'age_recommendation']