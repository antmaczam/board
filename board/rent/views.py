import string
import random

from django.shortcuts import render ,  get_object_or_404
from rent.models import Game
from django.conf import settings
from rent.forms import NewGame
from django.shortcuts import redirect

# Create your views here.
from rent.models import Rent
from user.models import User


def games_list(request):
    games = Game.objects.all()
    return render(request,'games.html',{'games':games})

def games_detail(request,pk):
     dato = get_object_or_404(Game, pk=pk)
     return render(request,'gameDetail.html', {'name':dato.name, 'description':dato.description,'price': dato.price ,
      'status': dato.status,'picture' : dato.picture,'owner': dato.owner })

def new_game(request):
    if request.method == "POST":
        form = NewGame(request.POST)
        if form.is_valid():
            Game = form.save(commit=False)

            Game.save()
            return redirect('/gameDetail/{}'.format(Game.id))
    else:
       form = NewGame()
    return render(request, 'newgame.html', {'form': form})
    
def edit_game(request, pk):
    juego = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = NewGame(request.POST, instance=juego)
        if form.is_valid():
            juego = form.save(commit=False)
            
            juego.save()
            return  redirect('/gameDetail/{}'.format(pk))
    else:
        form = NewGame(instance=juego)
    return render(request, 'newgame.html', {'form': form})
