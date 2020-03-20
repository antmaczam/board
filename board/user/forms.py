from django import forms

from .models import User
from django import forms



class NewUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name','email','bio','picture'  )