import string
import random
from datetime import date

from django.shortcuts import render ,  get_object_or_404
from rent.models import Game, Rent
from django.conf import settings
from rent.forms import NewGame
from django.shortcuts import redirect

# Create your views here.
from rent.models import Rent
from rent.models import Order
from rent.models import OrderItem
from user.models import User


def games_list(request):
    games = Game.objects.all()
    return render(request,'games.html',{'games':games})

def games_detail(request,pk):
     dato = get_object_or_404(Game, pk=pk)
     return render(request,'gameDetail.html', {'name':dato.name, 'description':dato.description,'price': dato.price ,
      'status': dato.status,'picture' : dato.picture,'owner': dato.owner, 'id':dato.id })

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
            return redirect('/gameDetail/{}'.format(pk))
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

def view_cart(request):
    user = get_object_or_404(User, pk=request.user.id)
    list_carts = Order.objects.filter(user=user)
    if not list_carts:
        ramdomLetters = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
        ramdomNumber = ''.join(random.choice(string.digits) for i in range(5))
        ref = ramdomLetters + '-' + ramdomNumber
        cart = Order(ref_code=ref, user=user, actual=True)
        cart.save()
        return render(request, 'orders.html', {'order': cart.items.all()})
    else:
        for c in list_carts:
            if c.actual:
                cart = c
                return render(request, 'orders.html', {'order': cart.items.all()})

def add_item_to_cart(request, id_game):
    dato = get_object_or_404(Game, pk=id_game)
    user = get_object_or_404(User, pk=request.user.id)
    list_carts = Order.objects.filter(user=user)
    if not list_carts:
        ramdomLetters = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
        ramdomNumber = ''.join(random.choice(string.digits) for i in range(5))
        ref = ramdomLetters + '-' + ramdomNumber
        cart = Order(ref_code=ref, user=user, actual=True)
        cart.save()
        añadir = True
        for item in cart.items.all():
            if item.game == dato:
                añadir = False
                break
        if añadir:
            item = OrderItem(game=dato, is_ordered=False, date_added=date.today())
            item.save()
            cart.items.add(item)
            cart.save()
        return render(request, 'orders.html', {'order': cart.items.all(), 'mensaje': 'Añadido con exito'})
    else:
        for c in list_carts:
            if c.actual:
                cart = c
                añadir = True
                for item in cart.items.all():
                    if item.game == dato:
                        añadir = False
                        return render(request, 'orders.html', {'order': cart.items.all(), 'mensaje': 'Item ya incluido en el carrito'})
                    if item.game.owner == user:
                        añadir = False
                        return render(request, 'orders.html', {'order': cart.items.all(), 'mensaje': 'No puedes comprar tu propio juego'})
                if añadir:
                    item = OrderItem(game=dato, is_ordered=False, date_added=date.today())
                    item.save()
                    cart.items.add(item)
                    cart.save()
                return render(request, 'orders.html', {'order': cart.items.all(), 'mensaje': 'Añadido con exito'})

def delete_item_from_cart(request, id_item):
    dato = get_object_or_404(OrderItem, pk=id_item)
    user = get_object_or_404(User, pk=request.user.id)
    list_carts = Order.objects.filter(user=user)
    for c in list_carts:
        if c.actual:
            cart = c
            for item in cart.items.all():
                if item == dato:
                    cart.items.remove(item)
                    dato.delete()
                    return render(request, 'orders.html', {'order': cart.items.all(), 'mensaje': 'Eliminado con exito'})
    return redirect('/cart')

def empty_cart(request):
    user = get_object_or_404(User, pk=request.user.id)
    list_carts = Order.objects.filter(user=user)
    for c in list_carts:
        if c.actual:
            cart = c
            for item in cart.items.all():
                cart.items.remove(item)
                item.delete()
    return render(request, 'orders.html', {'order': cart.items.all(), 'mensaje': 'Carrito vaciado'})