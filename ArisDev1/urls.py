"""ArisDev1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from ArisDev1 import views

urlpatterns = [ path('', views.index, name='index')
              , path('index/', views.index, name='index')
              , path('legalAdmin/', views.legalAdmin, name='legalAdmin')
              , path('retraites/', views.retraites, name='retraites')
              , path('activites/', views.activites, name='activites')
              , path('adherents/', views.adherents, name='adherents')
              , path('histoire/', views.histoire, name='histoire')
              , path('objetAris/', views.objetAris, name='objetAris')
              , path('offreAris/', views.offreAris, name='offreAris')
              , path('inscriptionAris/', views.inscriptionAris, name='inscriptionAris')
              , path('infosUtiles/', views.infosUtiles, name='infosUtiles')
              , path('statutsAris/', views.statutsAris, name='statutsAris')
              , path('conseilAdmin/', views.conseilAdmin, name='conseilAdmin')
              , path('assembleesGales/', views.assembleesGales, name='assembleesGales')
              , path('mentionsLegales/', views.mentionsLegales, name='mentionsLegales')
              , path('articlesRetraites/', views.articlesRetraites, name='articlesRetraites')
              , path('liensUtiles/', views.liensUtiles, name='liensUtiles')
              , path('programsActivites/', views.programsActivites, name='programsActivites')
              , path('comptesRendus/', views.comptesRendus, name='comptesRendus')
              , path('infosDiverses/', views.infosDiverses, name='infosDiverses')
              , path('petitesAnnonces/', views.petitesAnnonces, name='petitesAnnonces')
              , path('necrologie/', views.necrologie, name='necrologie')
              , path('spnConseilAdm/', views.spnConseilAdm, name='spnConseilAdm')
              , path('listAGO/', views.listAGO, name='listAGO')
              , path('carouselParis/', views.carouselParis, name='carouselParis')
              , path('admin/', admin.site.urls),
              ]
