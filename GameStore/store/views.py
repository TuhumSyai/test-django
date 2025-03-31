from django.shortcuts import render, HttpResponse
from .services.rawg import get_games
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Store")

def game_list(request):
    games = get_games()
    return JsonResponse(games, safe=False)