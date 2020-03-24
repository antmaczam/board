import string
import random

from django.shortcuts import render ,  get_object_or_404
from rent.models import Game, Rent
from django.conf import settings
from rent.forms import NewGame
from django.shortcuts import redirect

# Create your views here.
from rent.models import Rent
from user.models import User


def games_list(request):
    games = Game.objects.all()
    return render(request,'games.html',{'games':games})

def games_list_by_user(request):
    games = Game.objects.filter(owner=request.user)
    return render(request,'myGames.html',{'myGames':games})

def games_detail(request,pk):
     dato = get_object_or_404(Game, pk=pk)
     return render(request,'gameDetail.html', {'name':dato.name, 'description':dato.description,'price': dato.price ,
      'status': dato.status,'picture' : dato.picture,'owner': dato.owner, 'id':dato.id })
def delete_game(request, pk):
    # Recuperamos la instancia del juego y la borramos
    instancia = Game.objects.get(id=pk)
   
    if(instancia.owner == request.user):
        instancia.delete()
    return  redirect('/games')

    
def new_game(request):
    if request.method == "POST":
        form = NewGame(request.POST)
        if form.is_valid():
            Game = form.save(commit=False)
            Game.owner = request.user

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

def rent_game(request, id_game):
    dato = get_object_or_404(Game, pk=id_game)
    user = get_object_or_404(User, pk=request.user.id)
    letters = string.ascii_uppercase
    digits = string.digits
    ramdomLetters = ''.join(random.choice(letters) for i in range(3))
    ramdomNumber = ''.join(random.choice(digits) for i in range(4))
    ticker = ramdomLetters + '-' + ramdomNumber
    rent = Rent(ticker=ticker, game=dato, user= user, rentable=False)
    rent.save()
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})

def rents_list(request,id_user):
    rents = Rent.objects.filter(user=request.user)
    return render(request,'rents.html',{'rents':rents})