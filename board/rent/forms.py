from django import forms

from .models import Game
from django import forms



class NewGame(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'description','status','price','picture','address', )