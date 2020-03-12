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
from base import views as base_views

urlpatterns = [
    #Main
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', user_views.login),
    path('logout', user_views.logout),
    path('base/', views.base),
    #Rent
    path('games', rent_views.games_list),
    re_path(r'gameDetail/(?P<id_game>\d+)',rent_views.games_detail),
    #User
    re_path(r'profile/(?P<id_user>\d+)',user_views.profile),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
