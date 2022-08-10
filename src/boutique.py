#ici sont stockées les fonctions relatives à la boutique
from src.tipe_abeilles import *
from src.parametres import *
import random
import pygame


#fonction principale de la boutique où on peut acheter
def boutique(abeilles, miel, maxplaces, argent, nvIA):
    choix=1
    print("Bienvenue à la boutique !")
    while choix!=0:
        choix=int(input("Que voulez-vous acheter ? \n Tapez 1 pour agrandir votre ruche \n Tapez 2 pour acheter des abeilles \n Tapez 3 pour améliorer votre ruche \n Tapez 0 pour sortir de la boutique \n"))
        if choix==1:
            maxplaces, argent = agrandirRuche(maxplaces, argent)
            print("Nombre de places :", maxplaces, "\nArgent :", argent, "€")
        elif choix==2:
            if miel>=2 and (sommeAbeilles(abeilles)+100<=maxplaces):
                miel, abeilles = acheterAbeilles(abeilles, miel, maxplaces)
                print("Quantité de miel : ", miel, "kg")
                print("Abeilles :")
                for k in abeilles:
                    print(k)
            elif miel<2:
                print("Vous n'avez pas assez de miel pour pouvoir acheter des abeilles")
            else:
                print("Vous n'avez pas assez de places dans votre ruche pour acheter des abeilles")
        elif choix==3:
            nvIA = acheterIA(argent, nvIA)
        elif choix!=0 :
            print("Erreur de saisie, veuillez recommencer")
    return(nvIA)

#fonction pour agrandir la ruche
def agrandirRuche(maxplaces, argent):
    choix= float(input("Voulez-vous agrandir la ruche de 1000 places ? Prix : 100€ \n Oui : tapez 1 \n Non : tapez un autre chiffre \n"))
    if choix==1 and argent>=100:
        maxplaces+=1000
        argent=argent-100
    elif choix==1 and argent<100:
        print("Vous n'avez pas assez d'argent")
    return maxplaces, argent


#fonction pour acheter des abeilles
def acheterAbeilles(abeilles, miel, maxplaces):
    choix=1
    while choix!=0 and miel>=2 and (sommeAbeilles(abeilles)+100<=maxplaces):
        choix=int(input("Que voulez-vous faire ? \n Tapez 1 pour acheter 100 abeilles mâles - prix : 5kg miel \n Tapez 2 pour acheter 100 abeilles bâtisseuses - prix : 3kg miel \n Tapez 3 pour acheter 100 abeilles butineuses - prix : 2kg miel \n Tapez 4 pour acheter 100 abeilles ventileuses - prix : 3kg miel \n Tapez 5 pour acheter 100 abeilles gardiennes - prix : 5kg miel \n Tapez 0 pour sortir de ce menu \n"))
        if choix==1:
            if miel>=5 and (sommeAbeilles(abeilles)+100<=maxplaces):
                miel=miel-5
                abeilles[1]+=100
            elif miel<5:
                print("Vous n'avez pas assez de miel")
            else:
                print("Vous n'avez plus de places dans votre ruche")
        elif choix==2:
            if miel>=3 and (sommeAbeilles(abeilles)+100<=maxplaces):
                miel=miel-3
                abeilles[2]+=100
            elif miel<3:
                print("Vous n'avez pas assez de miel")
            else:
                print("Vous n'avez plus de places dans votre ruche")
        elif choix==3:
            if miel>=2 and (sommeAbeilles(abeilles)+100<=maxplaces):
                miel=miel-2
                abeilles[3]+=100
            elif miel<2:
                print("Vous n'avez pas assez de miel")
            else:
                print("Vous n'avez plus de places dans votre ruche")
        elif choix==4:
            if miel>=3 and (sommeAbeilles(abeilles)+100<=maxplaces):
                miel=miel-3
                abeilles[4]+=100
            elif miel<3:
                print("Vous n'avez pas assez de miel")
            else:
                print("Vous n'avez plus de places dans votre ruche")
        elif choix==5:
            if miel>=5 and (sommeAbeilles(abeilles)+100<=maxplaces):
                miel=miel-5
                abeilles[5]+=100
            elif miel<5:
                print("Vous n'avez pas assez de miel")
            else:
                print("Vous n'avez plus de places dans votre ruche")
        elif choix!=0 :
            print("Erreur de saisie, veuillez recommencer")
    return miel, abeilles


def conversionMiel(miel, pollen, argent):
    #Un gramme de miel contient en moyenne 5000 grains de pollen, ce qui donne environ 0,02g de pollen dans 100g de miel, soit une proportion de 0,02%
    miel+=pollen*0.02
    pollen=0
    return(miel, pollen, argent)


#Le prix du miel au kg change tous les jours
def changementPrix():
    prix=random.randrange(800, 1500, 1) / 100
    return(prix)

def conversionArgent(miel, pollen, argent):
    prix=changementPrix()
    estValide = 0
    print("Aujourd'hui, 1 kg de miel est vendu", prix, "€")
    print("Vous possédez ", miel, " kg de miel actuellement")
    while (estValide == 0) :
        nbMiel=int(input("Quelle quantité de miel voulez-vous vendre ? (en kg, nombre entier) \n"))
        if (nbMiel > miel) :
            print("Vous avez saisi une quantité de miel trop élevée...")
        elif (nbMiel == int(nbMiel)) :
            argent+=int(nbMiel*prix)
            miel-=nbMiel
            estValide = 1
        else:
            print("Merci de rentrer le résultat sous la forme d'un entier")
    return(miel, pollen, argent)

#procédure qui explique le rôle de chaque IA quand elle est achetée
def explication(nvIA, ecran):
    myfont = pygame.font.SysFont('rubikregular', 16)
    if nvIA==0:
        texte1 = myfont.render("Le niveau 1 d'IA permet :", False, (0, 0, 0))
        texte2 = myfont.render("-d'alerter si la température de la ruche est trop élevée ou faible", False, (0, 0, 0))
        texte3 = myfont.render("-d'alerter si une population d'abeilles s'est éteinte", False, (0, 0, 0))
        texte4 = myfont.render("-d'alrter s'il y a eu une forte diminution d'abeilles dans la journée", False, (0, 0, 0))
        ecran.blit(texte1,(300,530))
        ecran.blit(texte2,(300,545))
        ecran.blit(texte3,(300,560))
        ecran.blit(texte4,(300,575))
    if nvIA==1:
        texte = myfont.render("Le niveau 2 d'IA permet de mieux réguler la température de la ruche \n", False, (0, 0, 0))
        ecran.blit(texte,(300,545))
    if nvIA==2:
        texte = myfont.render("Le niveau 3 d'IA permet d'alerter s'il y a trop ou pas assez de miel \n", False, (0, 0, 0))
        ecran.blit(texte,(300,545))
    if nvIA==3:
        texte = myfont.render("Le niveau 4 d'IA permet de réduire les attaques \n", False, (0, 0, 0))
        ecran.blit(texte,(300,545))

# Fonction pour acheter les IA
def acheterIA(argent, nvIA):
    prix = 0 # prix de l'IA à acheter
    print("nvIA : ", nvIA)
    if (nvIA == 0) :
        prix = 400
    elif (nvIA == 1) :
        prix = 1500
    elif (nvIA == 2) :
        prix = 3000
    elif (nvIA == 0) :
        prix = 5000
    print("Le niveau ", nvIA + 1, " d'IA coûte ", prix, " €")
    if (argent >= prix) :
        choix = int(input("Souhaitez-vous l'acheter ? (tapez '1' pour oui)"))
        if (choix == 1) :
            nvIA += 1
            print("Vous avez acheté le niveau", nvIA, "d'IA !!!")
            explication(nvIA)
        elif (choix != 1) :
            print("Vous n'avez pas confirmé votre choix, vous retournez dans le menu de la boutique")
    elif (argent < prix) :
        print("Vous n'avez pas assez d'argent...")
    return (nvIA)
