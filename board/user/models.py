from django.db import models
from django.core.validators import URLValidator, validate_comma_separated_integer_list

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=32)
    bio = models.TextField(max_length=500)
    range = models. CharField(max_length=10)
    picture = models.CharField(max_length=500, validators=[URLValidator])
    rate = models. CharField(max_length=10, validators=[validate_comma_separated_integer_list])
    
    def __str__(self):
        return self.name