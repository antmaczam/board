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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from base import views
from user import views as user_views
from rent import views as rent_views
from reviews import views as reviews_views
from base import views as base_views


from rent.views import new_game
from rent import forms as rent_forms
from rent.forms import NewGame

urlpatterns = [
    #Main
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', user_views.login),
    path('logout', user_views.logout),
    path('base/', views.base),

    #Rent
    path('games/', rent_views.games_list),
    path('gameDetail/<int:pk>/', rent_views.games_detail, name='games_detail'),
    path('newgame', rent_views.new_game),
    path('gameDetail/<int:pk>/edit/', rent_views.edit_game, name='new_game'),
    re_path(r'rent/(?P<id_game>\d+)',rent_views.rent_game),
    re_path(r'rents/(?P<id_user>\d+)',rent_views.rents_list),

    #User
    re_path(r'profile/(?P<id_user>\d+)',user_views.profile),

    #Review
    re_path(r'review/(?P<id_user>\d+)',reviews_views.create_review),
    re_path(r'comments/(?P<id_user>\d+)',reviews_views.list_comments)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
