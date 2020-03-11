from django.shortcuts import render ,  get_object_or_404
from rent.models import Game
from django.conf import settings

# Create your views here.

def games_list(request):
    games = Game.objects.all()
    return render(request,'games.html',{'games':games})




def games_detail(request, id_game):
     dato = get_object_or_404(Game, pk=id_game)
     return render(request,'gameDetail.html', {'name':dato.name, 'description':dato.description,'price': dato.price ,
      'status': dato.status,'picture' : dato.picture,'owner': dato.owner })