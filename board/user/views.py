from django.shortcuts import render, get_object_or_404
from user.models import User

# Create your views here.

def profile(request, id_user):
     user = get_object_or_404(User, pk=id_user)
     return render(request,'profile.html', {'user':user})