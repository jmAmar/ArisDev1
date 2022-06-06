# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:58:31 2022

@author: JMichel
"""

from os import listdir
from os.path import isfile, join
#
from django.http import HttpResponse
from django.shortcuts import render
#import ArisDevt.fileManager as FM
#
def index(request):
    print("\t- index.html -")
    return render(request,'index.html')
#
def legalAdmin(request):
    print("\t- legalAdmin.html -")
    return render(request,'infosUtiles.html')
#
def retraites(request):
    print("\t- retraites.html -")
    return render(request,'articlesRetraites.html')
#
def activites(request):
    print("\t- activites.html -")
    return render(request,'programsActivites.html')
#
def adherents(request):
    print("\t- adherents.html -")
    return render(request,'infosDiverses.html')
#
def histoire(request):
    imgEmblemes = [f for f in listdir('./static/img/emblemesIndosuez') if isfile(join('./static/img/emblemesIndosuez', f))] ; imgEmblemes.sort()
    imgPnomPhen = [f for f in listdir('./static/img/indosuezPnomPhen') if isfile(join('./static/img/indosuezPnomPhen', f))] ; imgPnomPhen.sort()
    imgParis = [f for f in listdir('./static/img/indosuezParis') if isfile(join('./static/img/indosuezParis', f))] ; imgParis.sort()
    imgGorseHill = [f for f in listdir('./static/img/manoirGorseHill') if isfile(join('./static/img/manoirGorseHill', f))] ; imgGorseHill.sort()
    imgFillerval = [f for f in listdir('./static/img/chateauFillerval') if isfile(join('./static/img/chateauFillerval', f))] ; imgFillerval.sort()
    imgTremblay = [f for f in listdir('./static/img/domaineTremblay') if isfile(join('./static/img/domaineTremblay', f))] ; imgTremblay.sort()
    imgCommunication = [f for f in listdir('./static/img/comIndosuez') if isfile(join('./static/img/comIndosuez', f))] ; imgCommunication.sort()
    print("\t- histoire.html -")
    return render(request,'histoire.html', {'imgEmblemes':imgEmblemes, 'imgPnomPhen':imgPnomPhen, 'imgParis':imgParis
                                           , 'imgGorseHill':imgGorseHill, 'imgFillerval':imgFillerval, 'imgTremblay':imgTremblay
                                           , 'imgCommunication':imgCommunication
                                           })
#
def objetAris(request):
    print("\t- objetAris.html -")
    return render(request,'objetAris.html')
#
def offreAris(request):
    print("\t- offreAris.html -")
    return render(request,'offreAris.html')
#
def inscriptionAris(request):
    print("\t- inscriptionAris.html -")
    return render(request,'inscriptionAris.html')
#
def infosUtiles(request):
    print("\t- infosUtiles.html -")
    return render(request,'infosUtiles.html')
#
def statutsAris(request):
    print("\t- statutsAris.html -")
    return render(request,'statutsAris.html')
#
def conseilAdmin(request):
    print("\t- conseilAdmin.html -")
    return render(request,'conseilAdmin.html')
#
def assembleesGales(request):
    print("\t- assembleesGales.html -")
    return render(request,'assembleesGales.html')
#
def mentionsLegales(request):
    print("\t- mentionsLegales.html -")
    return render(request,'mentionsLegales.html')
#
def articlesRetraites(request):
    print("\t- articlesRetraites.html -")
    return render(request,'articlesRetraites.html')
#
def liensUtiles(request):
    print("\t- liensUtiles.html -")
    return render(request,'liensUtiles.html')
#
def programsActivites(request):
    print("\t- programsActivites.html -")
    return render(request,'programsActivites.html')
#{}
def comptesRendus(request):
    img20211015 = [f for f in listdir('./static/img/dejeuner20211015') if isfile(join('./static/img/dejeuner20211015', f))] ; img20211015.sort()
    imgPaysGalles = [f for f in listdir('./static/img/paysGalles') if isfile(join('./static/img/paysGalles', f))] ; imgPaysGalles.sort()
    imgVoyageVietnam = [f for f in listdir('./static/img/voyageVietnam') if isfile(join('./static/img/voyageVietnam', f))] ; imgVoyageVietnam.sort()
    imgEpiphanie2016 = [f for f in listdir('./static/img/epiphanie2016') if isfile(join('./static/img/epiphanie2016', f))] ; imgEpiphanie2016.sort()
    img20151009 = [f for f in listdir('./static/img/dejeuner20151009') if isfile(join('./static/img/dejeuner20151009', f))] ; img20151009.sort()
    imgEpiphanie2017 = [f for f in listdir('./static/img/epiphanie2017') if isfile(join('./static/img/epiphanie2017', f))] ; imgEpiphanie2017.sort()
    imgPortugal2017 = [f for f in listdir('./static/img/portugal2017') if isfile(join('./static/img/portugal2017', f))] ; imgPortugal2017.sort()
    imgEpiphanie2018 = [f for f in listdir('./static/img/epiphanie2018') if isfile(join('./static/img/epiphanie2018', f))] ; imgEpiphanie2018.sort()
    imgEpiphanie2019 = [f for f in listdir('./static/img/epiphanie2019') if isfile(join('./static/img/epiphanie2019', f))] ; imgEpiphanie2019.sort()
    img20181005 = [f for f in listdir('./static/img/dejeuner20181005') if isfile(join('./static/img/dejeuner20181005', f))] ; img20181005.sort()
    imgNamibie = [f for f in listdir('./static/img/namibie') if isfile(join('./static/img/namibie', f))] ; imgNamibie.sort()
    imgRajasthan = [f for f in listdir('./static/img/rajasthan') if isfile(join('./static/img/rajasthan', f))] ; imgRajasthan.sort()
    print("\t- comptesRendus.html -")
    return render(request,'comptesRendus.html', { 'img20211015': img20211015
                                                , 'imgPaysGalles':imgPaysGalles, 'imgVoyageVietnam':imgVoyageVietnam
                                                , 'img20151009':img20151009
                                                , 'imgEpiphanie2016':imgEpiphanie2016
                                                , 'imgEpiphanie2017':imgEpiphanie2017, 'imgPortugal2017':imgPortugal2017
                                                , 'imgEpiphanie2018':imgEpiphanie2018, 'img20181005':img20181005
                                                , 'imgEpiphanie2019':imgEpiphanie2019
                                                , 'imgNamibie':imgNamibie, 'imgRajasthan':imgRajasthan
                                                })
#
def infosDiverses(request):
    print("\t- infosDiverses.html -")
    return render(request,'infosDiverses.html')
#
def petitesAnnonces(request):
    print("\t- petitesAnnonces.html -")
    return render(request,'petitesAnnonces.html')
#
def necrologie(request):
    fchS = [f for f in listdir('./static/ncro') if isfile(join('./static/ncro', f))] ; fchS.sort(reverse=True)
    print("fchS: ",fchS)
    return render(request,'necrologie.html', {'fchS':fchS})
#
def spnConseilAdm(request):
    print("\t- infosUtiles.html#spnConseilAdm -")
    return render(request,'infosUtiles.html', {'anchor':'spnConseilAdm'})
#
def listAGO(request):
    fchS = [f for f in listdir('./static/ago') if isfile(join('./static/ago', f))] ; fchS.sort(reverse=True)
    print("fchS: ",fchS)
    return render(request,'assembleesGales.html', {'fchS':fchS})
#
def carouselParis(request):
    imgParis = [f for f in listdir('./static/img/indosuezParis') if isfile(join('./static/img/indosuezParis', f))] ; imgParis.sort()
    print("\t- carouselParis.html -")
    return render(request,'carouselParis.html',{'carouselParis':imgParis})
#