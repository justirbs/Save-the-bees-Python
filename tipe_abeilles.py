#TIPE save the bees! fcts abeilles
from math import *
from random import *

#calcule le nombre total d'abeilles
def sommeAbeilles(abeilles) :
    totalAbeilles = 0
    for i in abeilles :
        totalAbeilles += i
    return(totalAbeilles)


#renvoie la quantité de miel gagnée par jour, en kg, par rapport au nb de butineuses
def qtmiel(nbbuti):
    miel = pow(2*nbbuti/10000,2)
    return miel

#renvoie la populaion nouvelle journalière en fct du nb de mâles (sans compter danger, pertes, etc)
def reproduction(abeilles, tauxReproduction, maxplaces) :
    # on calcule les nouvelles naissances
    naissances = int(tauxReproduction * abeilles[1])
    # on répartie les naissances parmi les types d'abeilles
    abeilles[1] += int(0.05 * naissances)
    abeilles[2] += int(0.2 * naissances)
    abeilles[3] += int(0.5 * naissances)
    abeilles[4] += int(0.2 * naissances)
    abeilles[5] += int(0.05 * naissances)
    # si après la reproduction, le nombre d'abeilles est suppérieur au maximum de place dans la ruche, on réduit
    if sommeAbeilles(abeilles) > maxplaces:
        abeilles = (1, int(0.05*maxplaces), int(0.2*maxplaces), int(0.5*maxplaces), int(0.2*maxplaces), int(0.05*maxplaces))
    return(abeilles)

#donne la température du jour selon la température de la veille et la variation (croissante ou décroissante)
def temperatureJour(temperature, variation) :
    #si la température est très haute, on choisit de la diminuer
    if temperature > 40 :
        variation = -1
    #si la température est très basse, on choisit de l'augmenter
    elif temperature < 30 :
        variation = 1
    return(temperature + uniform(0, 2.5) * variation, variation)

#changement de température en fonction du nombre de ventileuses
def tempventil(nbventil, temp):
    if temp>35:
        temp=temp-(nbventil/8000)
    elif temp<35:
        temp=temp+(nbventil/8000)
    return temp

#répartit un nombre d'abeilles pour l'augmentation du nb grâce aux batisseuses
def repartir(abeilles, plusab):
    abeilles[1] += int(0.05*plusab)
    abeilles[2] += int(0.2*plusab)
    abeilles[3] += int(0.5*plusab)
    abeilles[4] += int(0.2*plusab)
    abeilles[5] += int(0.05*plusab)
    return abeilles

#agit seulement après un dégât de la ruche : augmentation de la santé de la ruche en fct des bâtisseuses
def batisseuses(abeilles, rsante):
    rsante = rsante + (abeilles[2]/200)
    if (rsante > 100) :
        rsante = 100
    return rsante

#réduction des dégâts lors d'attaques en fonction des gardiennes
def gardiennes(degat, nbgar):
    #le degat est mis en pourcentage
    degat=degat-(nbgar/50000)
    return degat
