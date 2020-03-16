import string
import random

from django.shortcuts import render ,  get_object_or_404
from rent.models import Game
from django.conf import settings

# Create your views here.
from rent.models import Rent
from user.models import User


def games_list(request):
    games = Game.objects.all()
    return render(request,'games.html',{'games':games})




def games_detail(request, id_game):
     dato = get_object_or_404(Game, pk=id_game)
     return render(request,'gameDetail.html', {'name':dato.name, 'description':dato.description,'price': dato.price ,
      'status': dato.status,'picture' : dato.picture,'owner': dato.owner })

def rent_game(request, id_game):
    dato = get_object_or_404(Game, pk=id_game)
    user = get_object_or_404(User, pk=request.user.id)
    letters = string.ascii_uppercase
    digits = string.digits
    ramdomLetters = ''.join(random.choice(letters) for i in range(3))
    ramdomNumber = ''.join(random.choice(digits) for i in range(4))
    ticker = ramdomLetters + '-' + ramdomNumber
    rent = Rent(ticker=ticker, game=dato, user= user, rentable=True)
    rent.save()
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

