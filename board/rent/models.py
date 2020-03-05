from django.db import models
from enum import Enum, auto
from django.core.validators import URLValidator, MaxValueValidator, MinValueValidator

# Create your models here.
"""
class Category(Enum):
    cooperativo = auto()
    terror = auto()
    aventura = auto()
"""

class Status(Enum):
    PE = 'Perfecto'
    FA = 'Faltan piezas'
    GA = 'Gastado'
    IN = 'Injugable'

#status = (('Pe','Perfecto'),('Fa','Faltan_piezas'),('Ga','Gastado'),('In','Injugable'))

class Game(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')
    status = models.CharField(max_length=20,choices=[(str(x),x.value) for x in Status])
    price = models.FloatField(default=0.0)
    picture = models.CharField(max_length=500,validators=[URLValidator])
    #rent
    address = models.CharField(max_length=100, default='')
    owner = models.CharField(max_length=50, default='admin')
    #category
    #reviews

    @classmethod
    def get_by_id(cls, cid):
        return Game.objects.get(pk=cid)
        

    def __unicode__(self):
        return '{}-{}'.format(self.get_name(),self.price)