"""raterproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from raterprojectapi.views.auth import login_user, register_user
from raterprojectapi.views.category import CategoryView
from raterprojectapi.views.game import GameView
from raterprojectapi.views.game_categories import GameCategoryView
from raterprojectapi.views.gamerating import GameRatingView
from raterprojectapi.views.gamereview import GameReviewView


router = routers.DefaultRouter(trailing_slash=False)
# 'games' is the url, GameView is what to display, 'game' is the base name used if an error occurs
router.register(r'games', GameView, 'game')
router.register(r'gamecategories', GameCategoryView, 'gamecategory')
router.register(r'categories', CategoryView, 'category')
router.register(r'gamereviews', GameReviewView, 'gamereview')
router.register(r'gameratings', GameRatingView, 'gamerating')



urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]