from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

from user.models import User
from user.forms import NewUser
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

def new_user(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
           
            User = form.save(commit=False)
            User.set_password(User.password)
            


            User.save()
            do_login(request, User)
            return redirect('/profile/{}'.format(User.id))
    else:
       form = NewUser()
    return render(request, 'newuser.html', {'form': form})
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
