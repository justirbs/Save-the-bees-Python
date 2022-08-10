from src.parametres import *
from src.tipe_abeilles import *
import pygame

#alerte le joueur si une population d'abeilles s'est éteinte
def popEteinte(ecran,abeilles):
    myfont = pygame.font.SysFont('rubikregular', 18)
    prob=0 #probleme, 1 si une population s'est éteinte, 0 sinon
    typ=-1 #type d'abeille
    #verification s'il manque une population
    for i in abeilles:
        if(i==0):
            prob=1
            typ=i
    #alerte au joueur
    if prob==1:
        if typ==abeilleMale:
            texteMale1 = myfont.render("Attention, vous n'avez plus d'abeilles", False, (0, 0, 0))
            ecran.blit(texteMale1,(550,130))
            texteMale2 = myfont.render("mâles !", False, (0, 0, 0))
            ecran.blit(texteMale2,(550,150))
        if typ==abeilleBat:
            texteTemp1 = myfont.render("Attention, vous n'avez plus d'abeilles", False, (0, 0, 0))
            ecran.blit(texteTemp1,(550,130))
            texteTemp2 = myfont.render("bâtisseuses !", False, (0, 0, 0))
            ecran.blit(texteTemp2,(500,150))
        if typ==abeilleBut:
            texteTemp1 = myfont.render("Attention, vous n'avez plus d'abeilles", False, (0, 0, 0))
            ecran.blit(texteTemp1,(550,130))
            texteTemp2 = myfont.render("butineuses !", False, (0, 0, 0))
            ecran.blit(texteTemp2,(500,150))
        if typ==abeilleVent:
            texteTemp1 = myfont.render("Attention, vous n'avez plus d'abeilles", False, (0, 0, 0))
            ecran.blit(texteTemp1,(550,130))
            texteTemp2 = myfont.render("ventileuses !", False, (0, 0, 0))
            ecran.blit(texteTemp2,(500,150))
        if typ==abeilleGard:
            texteTemp1 = myfont.render("Attention, vous n'avez plus d'abeilles", False, (0, 0, 0))
            ecran.blit(texteTemp1,(550,130))
            texteTemp2 = myfont.render("gardiennes !", False, (0, 0, 0))
            ecran.blit(texteTemp2,(500,150))

#alerte le joueur si la température est trop basse ou élevée
def tempDanger(ecran,temperature):
    myfont = pygame.font.SysFont('rubikregular', 18)
    if temperature>=39:
        texteTemp = myfont.render("La température est trop élevée !", False, (0, 0, 0))
        ecran.blit(texteTemp,(550,175))
    if temperature<=31:
        texteTemp = myfont.render("La température est trop basse !", False, (0, 0, 0))
        ecran.blit(texteTemp,(550,175))

#alerte le joueur si le niveau de miel est trop faible ou trop fort
def mielDanger(ecran,miel):
    myfont = pygame.font.SysFont('rubikregular', 18)
    if miel>=40 and miel<50:
        texteMiel = myfont.render("Votre ruche est bientôt saturée en miel !", False, (0, 0, 0))
        ecran.blit(texteMiel,(550,225))
    if miel>50:
        texteMiel = myfont.render("Votre ruche est saturée en miel !", False, (0, 0, 0))
        ecran.blit(texteMiel,(550,225))
    if miel<=10:
        texteMiel = myfont.render("Vos abeilles manquent de miel !", False, (0, 0, 0))
        ecran.blit(texteMiel,(550,225))


#alerte le joueur si son nombre d'abeilles a diminué fortement
def diminution(ecran,nbAb1, nbAb2):
    myfont = pygame.font.SysFont('rubikregular', 18)
    if (nbAb1-nbAb2)>=0 and (nbAb1-nbAb2)>=100 and nbAb2<(0.2*nbAb1):
        texteNbAb = myfont.render("Vous avez perdu beaucoup d'abeilles hier !", False, (0, 0, 0))
        ecran.blit(texteNbAb,(550,200))

#fonction principale de l'ia niveau 1
def niv1(ecran, abeilles, temperature, miel, nbAb1, nbAb2):
    popEteinte(ecran,abeilles)
    tempDanger(ecran,temperature)
    diminution(ecran,nbAb1, nbAb2)

#fonction principale de l'ia niveau 2
def niv2(ecran, temperature):
    return tempventil(20000, temperature)

#fonction principale de l'ia niveau 3
def niv3(ecran, miel):
   mielDanger(ecran,miel)

#fonction principale de l'ia niveau 4 (agit tous les 3 jours seulement !)
def niv4(ecran, tauxFrelons, tauxVarroa):
    tauxFrelons-=0.1
    tauxVarroa-=0.1
    return tauxFrelons, tauxVarroa
