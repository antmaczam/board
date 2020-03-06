from django.shortcuts import render
from rent.models import Game

# Create your views here.

def games_list(request):
    games = Game.objects.all()
    return render(request,'games.html',{'games':games})