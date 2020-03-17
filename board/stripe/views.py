from django.shortcuts import render
from stripe import views

def pago_completado(request):
    return render(request,'pago_completado.html')

def aceptacion_pago(request):
    return render(request,'aceptacion_pago.html') 