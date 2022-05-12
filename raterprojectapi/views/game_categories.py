"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import GameCategory


class GameCategoryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game_category = GameCategory.objects.get(pk=pk)
        serializer = GameCategorySerializer(game_category)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_categories = GameCategory.objects.all()
        serializer = GameCategorySerializer(game_categories, many=True)
        return Response(serializer.data)
    
class GameCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = GameCategory
        fields = ('id', 'game', 'category')
        depth = 1