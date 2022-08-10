from src.parametres import *
from src.tipe_abeilles import *
from src.interface import *
import random

# Fonction qui choisi aléatoirement le danger du jour
def choixDanger() :
    danger = randrange(4)
    return(danger)

# On réparti le nombre de morts entre les types d'abeilles sauf les abeilles butineuses qui sont parties butiner
def repartitionMortRuche(abeilles, taux) :
    abeilles[1] -= int(abeilles[1] * taux)
    abeilles[2] -= int(abeilles[2] * taux)
    abeilles[4] -= int(abeilles[4] * taux)
    abeilles[5] -= int(abeilles[5] * taux)
    return(abeilles)

# Fonction qui gère les attaques de frelons
def frelons(abeilles, tauxFrelons) :
    # les dégats seront plus ou moins élevés en fonctions des gardiennes
    tauxFrelons = gardiennes(tauxFrelons, abeilles[5])
    morts = sommeAbeilles(abeilles) * tauxFrelons
    abeilles = repartitionMortRuche(abeilles, tauxFrelons)
    return(abeilles)

# Fonction qui gère les invasions de varroa
def varroa(abeilles, tauxVarroa) :
    morts = sommeAbeilles(abeilles) * tauxVarroa
    abeilles = repartitionMortRuche(abeilles, tauxVarroa)
    return(abeilles)

# Fonction qui gère les variations de température
def dangerTemperature(abeilles, temperature) :
    # la température est plus ou moins régulée selon le nombre de ventileuses
    temperature = tempventil(abeilles[4], temperature)
    ecart = abs(35 - temperature)
    tauxTemp = ecart * 0.2 / 5
    abeilles = repartitionMortRuche(abeilles, tauxTemp)
    return(abeilles)

# Fonction qui gère les tempêtes
def tempete(abeilles, rsante, tauxTempete) :
    rsante -= rsante * tauxTempete
    return(rsante)

#Fonction qui gère tous les dangers du jour
def dangerJour(abeilles, temperature, rsante) :
    # les pertes liées aux variations de températures
    abeilles = dangerTemperature(abeilles, temperature)
    #on choisit un nombre aléatoire pour choisir le type de danger du jour
    danger = choixDanger()
    #si le danger vaut 0, il ne se passe rien : jour de chance ! Sinon :
    if danger == 1 :
        abeilles = frelons(abeilles, tauxFrelons)
    elif danger == 2 :
        abeilles = varroa(abeilles, tauxVarroa)
    elif danger == 3 :
        rsante = tempete(abeilles, rsante, tauxTempete)
    return(abeilles, rsante, danger)



#fonction qui laisse la possibilité que la reine meurt
def dangercritique(abeilles, rsante):
    res=5
    nbab=sommeAbeilles(abeilles)
    #rsante= santé de la ruche
    if (nbab>=5000 and nbab<7000)or(rsante>=40 and rsante<60):
        #une chance sur 3
        res=random.randint(0,2)
    elif (nbab>2000 and nbab<5000)or(rsante>20 and rsante<40):
        #une chance sur 2
        res=random.randint(0,1)
    elif (nbab<=2000)or(rsante<=20):
        res=1
    #si res vaut 1, la reine meurt
    return res


# Fonction qui nuit à la santé de la ruche si il n'y a pas assez de miel
def dangerMiel(rsante) :
    #print("\nIl n'y a pas assez de miel dans la ruche, cela nuit à sa santé")
    rsante -= rsante*0.1
    return(rsante)


# Fonction qui gère les conséquences de la pollution dans les champs
def dangerChamp(pollution, abeille, nbEnvoye) :
    #print("\nPollution du champ : ", pollution, "\nNombre d'abeilles mortes : ", pollution*nbEnvoye/100)
    abeilles[3] -= int(pollution*nbEnvoye/100)
    return(abeilles)

def dangerAugmente(tauxFrelons, tauxTempete, tauxVarroa, tauxReproduction, jour):
    #tous les 2 jours on augmente la difficulté du jeu
    if (jour%2)==0:
        if tauxFrelons<=0.7:
            tauxFrelons+=0.05
        if tauxVarroa<=0.7:
            tauxVarroa+=0.05
        if tauxTempete<=0.7:
            tauxTempete+=0.05
        if tauxReproduction>=1:
            tauxReproduction-=0.1
    return tauxFrelons, tauxTempete, tauxVarroa, tauxReproduction
