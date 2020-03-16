from django import forms


class ReviewForm(forms.Form):
    valoration = forms.FloatField(required = True, label='Puntuacion (De 0 a 5) ', initial=5.0)
    comment = forms.CharField(required = True, label='Comentario')