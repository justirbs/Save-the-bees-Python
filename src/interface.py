import pygame
from src.boutique import *


def afficherTexte(ecran, vie, miel, argent, temperature, jour) :
    myfont = pygame.font.SysFont('rubikregular', 22)
    texteVie = myfont.render(str(vie), False, (0, 0, 0))
    ecran.blit(texteVie,(90,14))
    texteMiel = myfont.render(str(miel)+" kg", False, (0, 0, 0))
    ecran.blit(texteMiel,(500,14))
    texteArgent = myfont.render(str(argent)+" €", False, (0, 0, 0))
    ecran.blit(texteArgent,(700,14))
    texteTemp = myfont.render(str(temperature)+" °C", False, (0, 0, 0))
    ecran.blit(texteTemp,(300,14))
    texteJour = myfont.render("Jour : "+str(jour), False, (0, 0, 0))
    ecran.blit(texteJour,(780,14))

def afficherInfo(ecran, x, y, champs, boutique, nbMale, nbGardienne, nbVentileuse, nbBatisseuse,nbButineuse, tailleRuche, niveauIA, totalAbeilles):
    myfont = pygame.font.SysFont('rubikregular', 18)
    if(x>247 and x<323 and y>150 and y<223 and boutique == 0 and champs == 0) :
        #afficher texte
        texteMale = myfont.render('Abeilles Males : '+str(nbMale), False, (0, 0, 0))
        ecran.blit(texteMale,(331,175))
    if(x>414 and x<521 and y>235 and y<324 and boutique == 0 and champs == 0) :
        #afficher texte
        texteGardienne = myfont.render('Abeilles Gardiennes : '+str(nbGardienne), False, (0, 0, 0))
        ecran.blit(texteGardienne,(526,272))
    if(x>538 and x<623 and y>332 and y<409 and boutique == 0 and champs == 0) :
        #afficher texte
        texteVentileuse = myfont.render('Abeilles Ventileuses : '+str(nbVentileuse), False, (0, 0, 0))
        ecran.blit(texteVentileuse,(625,365))
    if(x>273 and x<344 and y>407 and y<488 and boutique == 0 and champs == 0) :
        #afficher texte
        texteBatisseuse = myfont.render('Abeilles Batisseuses : '+str(nbBatisseuse), False, (0, 0, 0))
        ecran.blit(texteBatisseuse,(65,445))
    if(x>660 and x<743 and y>523 and y<600 and boutique == 0 and champs == 0) :
        #afficher texte
        texteButineuse = myfont.render('Abeilles Butineuses : '+str(nbButineuse), False, (0, 0, 0))
        ecran.blit(texteButineuse,(631,500))
    if(x>349 and x<481 and y>355 and y<570 and boutique == 0 and champs == 0) :
        #afficher texte
        texteNiveau = myfont.render('Taille de la ruche : '+str(tailleRuche), False, (0, 0, 0))
        ecran.blit(texteNiveau,(500,462))
        texteIA = myfont.render("Niveau de l'IA : "+str(niveauIA), False, (0, 0, 0))
        ecran.blit(texteIA,(500,480))
    texteTotalAbeilles = myfont.render("Total : "+str(totalAbeilles), False, (0, 0, 0))
    ecran.blit(texteTotalAbeilles,(380,520))

def afficherInfoBoutique(ecran, x, y, nbMale, nbGardienne, nbVentileuse, nbBatisseuse,nbButineuse, tailleRuche, niveauIA, prixMiel, prixIA, miel,argent):
    myfont = pygame.font.SysFont('rubikregular', 18)
    if(x>63 and x<149 and y>201 and y<278) :
        #afficher texte
        texteMale = myfont.render('Abeilles Males : '+str(nbMale), False, (0, 0, 0))
        ecran.blit(texteMale,(49,287))
        textePrix = myfont.render('Prix = 5 kg miel / 100 abeilles', False, (0, 0, 0))
        ecran.blit(textePrix,(49,302))
        if (miel<5):
            textePrix = myfont.render("Vous n'avez pas assez de miel", False, (0, 0, 0))
            ecran.blit(textePrix,(49,317))

    if(x>516 and x<609 and y>155 and y<242) :
        #afficher texte
        texteGardienne = myfont.render('Abeilles Gardiennes : '+str(nbGardienne), False, (0, 0, 0))
        ecran.blit(texteGardienne,(490,257))
        textePrix = myfont.render('Prix = 5 kg miel / 100 abeilles', False, (0, 0, 0))
        ecran.blit(textePrix,(470,272))
        if (miel<5):
            textePrix = myfont.render("Vous n'avez pas assez de miel", False, (0, 0, 0))
            ecran.blit(textePrix,(470,287))

    if(x>332 and x<434 and y>209 and y<310) :
        #afficher texte
        texteVentileuse = myfont.render('Abeilles Ventileuses : '+str(nbVentileuse), False, (0, 0, 0))
        ecran.blit(texteVentileuse,(437,277))
        textePrix = myfont.render('Prix = 3 kg miel / 100 abeilles', False, (0, 0, 0))
        ecran.blit(textePrix,(437,292))
        if (miel<3):
            textePrix = myfont.render("Vous n'avez pas assez de miel", False, (0, 0, 0))
            ecran.blit(textePrix,(437,307))

    if(x>705 and x<791 and y>228 and y<313) :
        #afficher texte
        texteBatisseuse = myfont.render('Abeilles Batisseuses : '+str(nbBatisseuse), False, (0, 0, 0))
        ecran.blit(texteBatisseuse,(620,319))
        textePrix = myfont.render('Prix = 3 kg miel / 100 abeilles', False, (0, 0, 0))
        ecran.blit(textePrix,(620,334))
        if (miel<3):
            textePrix = myfont.render("Vous n'avez pas assez de miel", False, (0, 0, 0))
            ecran.blit(textePrix,(600,349))

    if(x>253 and x<346 and y>102 and y<196) :
        #afficher texte
        texteButineuse = myfont.render('Abeilles Butineuses : '+str(nbButineuse), False, (0, 0, 0))
        ecran.blit(texteButineuse,(331,129))
        textePrix = myfont.render('Prix = 2 kg miel / 100 abeilles', False, (0, 0, 0))
        ecran.blit(textePrix,(341,144))
        if (miel<2):
            textePrix = myfont.render("Vous n'avez pas assez de miel", False, (0, 0, 0))
            ecran.blit(textePrix,(341,159))

    if(x>120 and x<339 and y>370 and y<547) :
        #afficher texte
        texteTaille = myfont.render('Taille de la ruche : '+str(tailleRuche), False, (0, 0, 0))
        ecran.blit(texteTaille,(343,419))
        textePrix = myfont.render('Prix = 100 € / 1000 places', False, (0, 0, 0))
        ecran.blit(textePrix,(343,434))
        if (argent<100):
            textePrix = myfont.render("Vous n'avez pas assez d'argent", False, (0, 0, 0))
            ecran.blit(textePrix,(343,448))

    if(x>616 and x<746 and y>370 and y<547) :
        #afficher texte
        texteIA = myfont.render("Niveau de l'IA : "+str(niveauIA), False, (0, 0, 0))
        ecran.blit(texteIA,(470,413))
        explication(niveauIA, ecran)
        if(niveauIA < 4):
            textePrix = myfont.render('Prix = '+str(prixIA)+' € ', False, (0, 0, 0))
            textePrix2 = myfont.render('pour le niveau '+str(niveauIA+1),False, (0,0,0,))
            ecran.blit(textePrix,(470,438))
            ecran.blit(textePrix2,(470,453))
        if(niveauIA==4):
            texteIA2 = myfont.render("Niveau maximum",False, (0,0,0,))
            ecran.blit(texteIA2,(470,428))
        if (argent<prixIA):
            textePrix = myfont.render("Vous n'avez pas assez d'argent", False, (0, 0, 0))
            ecran.blit(textePrix,(380,468))

    if(x>493 and x<638 and y>54 and y<110) :
        #afficher texte
        texteMiel = myfont.render("Changer miel en argent,", False, (0, 0, 0))
        texteMiel2 = myfont.render("1 kg de miel rapporte : "+str(prixMiel)+" €", False, (0, 0, 0))
        ecran.blit(texteMiel,(439,106))
        ecran.blit(texteMiel2,(439,121))
        if (miel<1):
            textePrix = myfont.render("Vous n'avez pas assez de miel", False, (0, 0, 0))
            ecran.blit(textePrix,(439,136))

def choixNbAbeille (ecran, nbAbeille, nbChamp):
    x, y = pygame.mouse.get_pos()
    myfont = pygame.font.SysFont('rubikregular', 18)
    if(nbChamp == 1):
        texte1 = myfont.render("Choisissez le nombre d'abeilles que vous voulez envoyer au champ du Moulin", False, (0, 0, 0))
    elif(nbChamp == 2):
        texte1 = myfont.render("Choisissez le nombre d'abeilles que vous voulez envoyer au champ de la Ferme", False, (0, 0, 0))
    elif(nbChamp == 3):
        texte1 = myfont.render("Choisissez le nombre d'abeilles que vous voulez envoyer au champ du Soleil", False, (0, 0, 0))

    texte2 = myfont.render(str(nbAbeille), False, (0, 0, 0))
    ecran.blit(texte1,(120,220))
    ecran.blit(texte2,(418,293))

def Fctchamps():
    jeu_en_cours = True
    while jeu_en_cours :
        x, y = pygame.mouse.get_pos()


def afficherDanger(ecran, danger):
    myfont = pygame.font.SysFont('rubikregular', 22)
    if danger == 0:
        texteDanger = myfont.render("Il n'y a pas eu de danger aujourd'hui", False, (0, 0, 0))
        ecran.blit(texteDanger,(550,130))
    elif danger == 1:
        texteDanger = myfont.render("Une attaque de frelons a lieu !!!", False, (0, 0, 0))
        ecran.blit(texteDanger,(550,130))
    elif danger == 2:
        texteDanger = myfont.render("Une invasion de varroa a lieu !!!", False, (0, 0, 0))
        ecran.blit(texteDanger,(550,130))
    elif danger == 3:
        texteDanger = myfont.render("Une tempête a lieu !!!", False, (0, 0, 0))
        ecran.blit(texteDanger,(550,130))
    elif danger == -1:
        texteDanger = myfont.render("", False, (0, 0, 0))
        ecran.blit(texteDanger,(550,130))


def afficherOrdreChamp(ecran):
    image = pygame.image.load("img/fleche.png").convert_alpha()
    ecran.blit(image, (100,190))

def afficherOrdreBoutique(ecran):
    image = pygame.image.load("img/fleche.png").convert_alpha()
    ecran.blit(image, (100,290))


def afficherPollutionChamp(ecran):
    myfont = pygame.font.SysFont('rubikregular', 22)
    textePollution = myfont.render("Le champ était pollué !", False, (0, 0, 0))
    ecran.blit(textePollution,(550,155))






if __name__ == "__main__":
    main()
