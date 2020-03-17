import random
from django.test import TestCase

from user.models import User
from rent.models import Game, Status

class GameModelTestCase(TestCase):
    
    #Prepara una bbdd default con los objetos que se van a testear en este TestCase -------------------

    def setUp(self):
        self.user = User(username='prueba',password='prueba123')
        self.user.save()
        
        self.game = Game(name='BANG',description='descripcion',status=Status.PE,price=2.5,picture='http://www.foto,com/foto,png',address='Los remedios',owner=self.user)
        self.game.save()
    
    #Batería de test unitarios ------------------------------------------------------------------------

    def test_get_owner(self):
        self.assertEquals(self.game.owner,self.user)
    
    def test_get_name(self):
        self.assertEquals(self.game.name,'BANG')

    #Borra los datos para terminar con los test ------------------------------------------------------
    
    def tearDown(self):
        self.game.delete()
        self.user.delete()