"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path
from rent import views as rent_views
from base import views as base_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rent.views import new_game
from rent import forms as rent_forms
from rent.forms import NewGame
urlpatterns = [
    path('admin/', admin.site.urls),
    path('games', rent_views.games_list),
    path('rents', rent_views.rents_list),
    path('gameDetail/<int:pk>/', rent_views.games_detail, name='games_detail'),
    path('',base_views.index),
    path('base/', base_views.base),
    path('newgame', rent_views.new_game),
    path('delete/<int:pk>', rent_views.delete),
    path('gameDetail/<int:pk>/edit/', rent_views.edit_game, name='new_game')
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

