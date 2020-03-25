from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from rent.models import Game
from rent.views import rent_game
import stripe

def pay(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request,'home.html',{'key':key})

def charge(request,id_game):
    game = get_object_or_404(Game, pk=id_game)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=int(game.price*100),
            currency='eur',
            description='A Django charge',
            source=request.POST['stripeToken'],
            api_key=settings.STRIPE_SECRET_KEY
        )
        rent_game(request,id_game)
        return redirect('/success/')

def pago_completado(request):
    return render(request,'pago_completado.html')

def confirm(request,id_game):
    game = get_object_or_404(Game, pk=id_game)
    cent = int(game.price*100)
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request,'aceptacion_pago.html',{'game':game,'key':key, 'cent':cent}) 