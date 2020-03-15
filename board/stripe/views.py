from django.shortcuts import render

# Create your views here.

def aceptacion_pago(request):
    return render(request,'aceptacion_pago.html')

def pago_completado(request):
    return render(request,'pago_completado.html')    