from parametres import *
from dangers import *
from tipe_abeilles import *
from boutique import*
from ia import *
from champs import *
import pygame
from interface import *



#fonction qui indique quand est-ce que la partie est perdue
def aPerdu(abeilles, jours, rsante):
    res = 0
    if dangercritique(abeilles, rsante)==1:
        print("La reine des abeilles est morte ! C'est la fin de la partie, vous perdez. Votre ruche a survécu",jours, "jours")
        res = 1
    return res


# Fonction qui active les IA que possède le joueur
def activeIA(ecran,abeilles, temperature, miel, nbAb1, nbAb2, tauxFrelons, tauxVarroa, jour) :
    if nvIA >= 4 and (jour%3)==0:
        niv4(ecran, tauxFrelons,tauxVarroa)
    if nvIA >= 3 :
        niv3(ecran, miel)
    if nvIA >= 2 :
        niv2(ecran, temperature)
    if nvIA >= 1 :
        niv1(ecran, abeilles, temperature, miel, nbAb1, nbAb2)





pygame.init()

#parametre de la fenetre
taille_ecran = (859, 640)
ecran = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption("Save the bees !")
image = pygame.image.load("Abeille.png").convert()
pygame.display.set_icon(image)
#Image
image = pygame.image.load("accueil.png").convert_alpha()
#texte
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('rubikregular', 18)
# frames par second
FPS = 20
fpsClock = pygame.time.Clock()

#variables
boutique = 0
champs = 0
danger = -1
choix = 0
nbAbeille = 100
defaite = 0
accueil = 0

boutique_ok = 0
champs_ok = 1
temperature_ok = 0
danger_ok = 1
polution_ok = 0

# Fonctions pour fixer les variables en fin de journée
def finJournee():
    boutique_ok = 0
    champs_ok = 1
    temperature_ok = 0
    danger_ok = 1
    danger = -1
    polution_ok = 0
    return(boutique_ok, champs_ok, temperature_ok, danger_ok, danger, polution_ok)

#variable qui me permet qui me permet de maintenir la boucle
jeu_en_cours = True

# tant que la variable jeu_en_cours sera vrai, la boucle maintiendra la fenêtre ouverte
while jeu_en_cours :
    ecran.blit(image, (0, 0))
    events = pygame.event.get()
    #image en arrière plan
    x, y = pygame.mouse.get_pos()
    for event in events:
        if (event.type == pygame.MOUSEBUTTONDOWN and x>277 and x<579 and y>450 and y<535 and accueil ==0):
            image = pygame.image.load("ecranAccueil.png").convert_alpha()
            accueil = 1

    #info en haut de l'écran
    if(accueil == 1):
        afficherTexte(ecran, round(rsante, 2), round(ressource[0], 2), round(ressource[2], 2), round(temperature, 2), jour)

    #on fait varier la température
    if(temperature_ok == 0):
        temperature, variation = temperatureJour(temperature, variation)
        temperature_ok = 1

    #le danger du jour a lieu
    if(danger_ok == 0):
        abeilles, rsante, danger = dangerJour(abeilles, temperature, rsante)
        danger_ok = 1

    if(boutique == 0 and champs == 0 and accueil==1):
        afficherDanger(ecran, danger)

    if(boutique_ok == 1 and boutique == 0 and champs == 0 and choix == 0 and accueil==1):
        afficherOrdreBoutique(ecran)

    if(champs_ok == 1 and boutique == 0 and champs == 0 and choix == 0 and accueil==1):
        afficherOrdreChamp(ecran)

    # on vérifie qu'il n'y ait pas trop de miel dans la ruche
    if ressource[0]>maxMiel:
        maxMiel_ok = 1
        champs_ok = 0
        boutique_ok = 1
    else:
        maxMiel_ok = 0


    #position souris
    x, y = pygame.mouse.get_pos()

    if(boutique == 0 and champs == 0 and choix == 0 and accueil==1):
        activeIA(ecran,abeilles, temperature, ressource[0], nbAb1, nbAb2, tauxFrelons, tauxVarroa, jour)
        afficherInfo(ecran, x, y, champs, boutique,abeilles[1], abeilles[5], abeilles[4], abeilles[2],abeilles[3], maxplaces, nvIA, sommeAbeilles(abeilles))

    if(x>13 and x<88 and y>177 and y<247 and champs == 0 and boutique == 0 and choix == 0 and accueil==1) :
        #afficher texte
        texteChamps = myfont.render('Champs', False, (0, 0, 0))
        ecran.blit(texteChamps,(18,155))

        #action lors du clic
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN) and (champs_ok == 1) :
                image = pygame.image.load("ecranChamps.png").convert_alpha()
                if ressource[0] < minMiel:
                    rsante = dangerMiel(rsante)
                champs = 1
                #action

    if(x>12 and x<82 and y>276 and y<341 and boutique == 0 and champs == 0 and choix == 0 and accueil==1) :
        texteBoutique = myfont.render('boutique', False, (0, 0, 0)) #afficher texte
        ecran.blit(texteBoutique,(14,344))

        #action lors du clic
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN) and (boutique_ok == 1) :
                image = pygame.image.load("ecranBoutique.png").convert_alpha()
                boutique = 1
                # on calcule le prix du miel
                prix=changementPrix()

    if (champs == 1):
        if(x>282 and x<548 and y>97 and y<264 and champs == 1) :
            #action
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    image = pygame.image.load("fond.png").convert_alpha()
                    champs = 0
                    choix = 1
                    nbChamp = 1

        if(x>62 and x<321 and y>327 and y<470 and champs == 1) :
            #action
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN :
                    image = pygame.image.load("fond.png").convert_alpha()
                    champs = 0
                    choix = 1
                    nbChamp = 3

        if(x>515 and x<756 and y>310 and y<468 and champs == 1) :
            #action
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN :
                    image = pygame.image.load("fond.png").convert_alpha()
                    champs = 0
                    choix = 1
                    nbChamp = 2

        if(x>0 and x<50 and y>0 and y<50 and champs == 1) :
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN :
                    image = pygame.image.load("ecranAccueil.png").convert_alpha()
                    champs = 0

    if (choix == 1 and boutique == 0 and champs == 0):
        pollution=pollueChamp(*pollution)
        tauxPollen=pollenChamp(*tauxPollen)
        choixNbAbeille(ecran, nbAbeille, nbChamp)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN :
                x, y = pygame.mouse.get_pos()
            if (event.type == pygame.MOUSEBUTTONDOWN and x>353 and x<382 and y>283 and y<310 and (nbAbeille < abeilles[3])) :
                nbAbeille = nbAbeille + 100
            if (event.type == pygame.MOUSEBUTTONDOWN and x>477 and x<505 and y>288 and y<315 and nbAbeille>0) :
                nbAbeille = nbAbeille - 100
            if (event.type == pygame.MOUSEBUTTONDOWN and x>380 and x<471 and y>360 and y<401) :
                #action
                image = pygame.image.load("ecranAccueil.png").convert_alpha()
                abeilles = dangerChamp(pollution[nbChamp-1], abeilles, nbAbeille)
                if pollution[nbChamp-1] != 0 :
                    polution_ok = 1
                pollenCollecte = recoltePollen(ressource[0], ressource[1], ressource[2], tauxPollen[nbChamp-1], nbAbeille)
                ressource = (ressource[0], pollenCollecte, ressource[2])
                ressource=conversionMiel(*ressource)
                activeIA(ecran,abeilles, temperature, ressource[0], nbAb1, nbAb2, tauxFrelons, tauxVarroa, jour)
                nbAbeille = 100
                choix = 0
                boutique_ok = 1
                champs_ok = 0
                danger_ok = 0

    if(polution_ok == 1 and boutique == 0):
        afficherPollutionChamp(ecran)


    if (boutique == 1):
        # on calcule le prix de l'IA
        if (nvIA == 0) :
            prixIA = 400
        elif (nvIA == 1) :
            prixIA = 1500
        elif (nvIA == 2) :
            prixIA = 3000
        elif (nvIA == 3) :
            prixIA = 5000
        afficherInfoBoutique(ecran, x, y, abeilles[1], abeilles[5], abeilles[4], abeilles[2],abeilles[3], maxplaces, nvIA, prix, prixIA, ressource[0],ressource[2])
        for event in events:
            # pour acheter des abelles mâles
            if (event.type == pygame.MOUSEBUTTONDOWN and x>63 and x<149 and y>201 and y<278 and boutique == 1 and ressource[0]>=5 and sommeAbeilles(abeilles)<maxplaces):
                abeilles[1] += 100
                ressource = (ressource[0]-5, ressource[1], ressource[2])
            # pour acheter des abelles gardiennes
            if (event.type == pygame.MOUSEBUTTONDOWN and x>516 and x<609 and y>155 and y<242 and boutique == 1 and ressource[0]>=5 and sommeAbeilles(abeilles)<maxplaces):
                abeilles[5] += 100
                ressource = (ressource[0]-5, ressource[1], ressource[2])
            # pour acheter des abelles ventileuses
            if (event.type == pygame.MOUSEBUTTONDOWN and x>332 and x<434 and y>209 and y<310 and boutique == 1 and ressource[0]>=3 and sommeAbeilles(abeilles)<maxplaces):
                abeilles[4] += 100
                ressource = (ressource[0]-3, ressource[1], ressource[2])
            # pour acheter des abelles batisseuses
            if (event.type == pygame.MOUSEBUTTONDOWN and x>705 and x<791 and y>228 and y<313 and boutique == 1 and ressource[0]>=3 and sommeAbeilles(abeilles)<maxplaces):
                abeilles[2] += 100
                ressource = (ressource[0]-3, ressource[1], ressource[2])
            # pour acheter des abelles butineuses
            if (event.type == pygame.MOUSEBUTTONDOWN and x>253 and x<346 and y>102 and y<196 and boutique == 1 and ressource[0]>=2 and sommeAbeilles(abeilles)<maxplaces):
                abeilles[3] += 100
                ressource = (ressource[0]-2, ressource[1], ressource[2])
            # pour agrandir la taille de la ruche
            if (event.type == pygame.MOUSEBUTTONDOWN and x>120 and x<339 and y>370 and y<547 and boutique == 1 and ressource[2]>=100):
                maxplaces += 1000
                ressource = (ressource[0], ressource[1], ressource[2]-100)
            # pour convertir le miel en argent
            if (event.type == pygame.MOUSEBUTTONDOWN and x>493 and x<638 and y>54 and y<110 and boutique == 1 and ressource[0]>=1):
                ressource = (ressource[0]-1, ressource[1], ressource[2]+prix)
            # pour acheter un nouveau niveau d'IA
            if (event.type == pygame.MOUSEBUTTONDOWN and x>616 and x<746 and y>370 and y<547 and boutique == 1 and ressource[2]>=prixIA):
                ressource = (ressource[0], ressource[1], ressource[2]-prixIA)
                if(nvIA<4):
                    nvIA += 1
                    explication(nvIA,ecran)

            # pour sortir de la boutique
            if (event.type == pygame.MOUSEBUTTONDOWN and x>764 and x<823 and y>70 and y<162 and boutique == 1)  :
                image = pygame.image.load("ecranAccueil.png").convert_alpha()
                if maxMiel_ok:
                    abeilles = repartitionMortRuche(abeilles, 0.3)
                    abeilles[5] -= int(abeilles[5]*0.3)
                #on fixe toutes les variables
                boutique_ok, champs_ok, temperature_ok, danger_ok, danger, polution_ok = finJournee()
                rsante = batisseuses(abeilles, rsante)
                abeilles = reproduction(abeilles, tauxReproduction, maxplaces)
                # on calcule le nombre d'abeilles le soir àprès la reproduction
                nbAb2=sommeAbeilles(abeilles)
                jour += 1
                # on calcule le nombre d'abeilles le matin
                nbAb1=sommeAbeilles(abeilles)
                boutique = 0
                tauxFrelons, tauxTempete, tauxVarroa, tauxReproduction=dangerAugmente(tauxFrelons, tauxTempete, tauxVarroa, tauxReproduction, jour)
                defaite = aPerdu(abeilles, jour, rsante)


    if defaite == 1:
        accueil = 0
        image = pygame.image.load("fond2.png").convert_alpha()
        textePerdu = myfont.render("La reine des abeilles est morte ! C'est la fin de la partie, vous perdez.", False, (0, 0, 0)) #afficher texte
        textePerdu2 = myfont.render("Votre ruche a survécu "+str(jour)+" jours",False, (0, 0, 0))
        ecran.blit(textePerdu,(170,220))
        ecran.blit(textePerdu2,(300,300))



    #conditions d'arrêt
    for event in events:
        if event.type == pygame.QUIT:
            jeu_en_cours = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jeu_en_cours = False


    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()
