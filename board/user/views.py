from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.hashers import check_password
from django import forms

from user.models import User
from user.forms import NewUser, Register
from reviews.models import Valoration, Comment


# Create your views here.

def profile(request, id_user):
     user = get_object_or_404(User, pk=id_user)
     list_comments = Comment.objects.filter(toUser=user)
     return render(request,'profile.html', {'user':user},{'comments': list_comments})

def logout(request):
     do_logout(request)
     return redirect('/')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def delete_myUSer(request, pk):
    # Recuperamos la instancia del user y la borramos
    instancia = User.objects.get(id=pk)
    if(instancia == request.user):
        instancia.delete()
        return redirect('/')
  
    
    return redirect('/')
def edit_user(request, pk):
    # Recuperamos la instancia de la persona
    instancia = User.objects.get(id=pk)

    # Creamos el formulario con los datos de la instancia
    form = NewUser(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = NewUser(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return  redirect('/profile/{}'.format(pk))

    # Si llegamos al final renderizamos el formulario
    return render(request, "newuser.html", {'form': form})

def new_user(request):
    if(request.method=='POST'):
        formulario = Register(request.POST)
        if(formulario.is_valid()):
            if (formulario.cleaned_data['password1']!=formulario.cleaned_data['password2']):
               formulario.add_error('password2','no coinciden las contraseñas')
               return render(request,"newuser.html",{"form":formulario})
            user = User(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            user.set_password(user.password)
            user.save()
            do_login(request, user)
            return redirect('/profile/{}'.format(user.id))
    else:
        formulario = Register()
    return render(request,"newuser.html",{"form":formulario})