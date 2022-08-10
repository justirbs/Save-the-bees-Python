#TIPE save the bees; gestion des ressources
import math
import random
from src.parametres import *
from src.boutique import *
from src.dangers import *




def pollenChamp(*tauxPollen):
	qte1 = random.randint(0,100)
	qte2 = random.randint(0,100)
	qte3 = random.randint(0,100)
	tauxPollen = (qte1, qte2, qte3)
	return(tauxPollen)

def pollueChamp(*pollution):
	x=random.randint(0, 2) #seul un des champs est pollué
	if x==0: #taux de pollution des champs établit
		pollution = (random.randint(0,100), 0, 0)
	if x==1:
		pollution = (0,random.randint(0,100), 0)
	if x==2:
		pollution = (0, 0, random.randint(0,100))
	#print("\nLe champ "+str(x+1)+" est pollué !")
	return(pollution)


def recoltePollen(miel, pollen, argent, tauxRecolte, nombreAbeille):
	pollen+=nombreAbeille*tauxRecolte/200
	return(pollen)


def envoyerAbeilles(miel, pollen, argent, abeilles, pollution, *tauxPollen): #le nombre d'abeille sert à ce que le joueur n'envoie pas plus d'abeille qu'il n'en possède
	nombreAbeille = abeilles[3]
	envoi=[0,0,0]
	pollenCollecte=0
	for x in range(0,3):
		while True:
			print("Nombre d'abeilles butineuses disponibles : "+str(nombreAbeille))
			ordreEnvoi = int(input("Combien d'abeilles voulez-vous envoyer dans le champ "+str(x+1)+" ? "))
			if nombreAbeille >= ordreEnvoi:
				envoi[x] = ordreEnvoi
				abeilles = dangerChamp(pollution[x], abeilles, ordreEnvoi)
				nombreAbeille-= ordreEnvoi
				break
			else :
				print("erreur, nombre d'abeille trop grand")
	for i in range(0, 3):
		pollenCollecte+=recoltePollen(miel, pollen, argent, tauxPollen[i], envoi[i])
	print("nombre de pollen collecte durant l'expédition : "+str(pollenCollecte)+" !")
	ressource = (miel, pollenCollecte, argent)
	return (ressource, abeilles)



# Fonction pour gérer ce qu'il se passe au niveau des champs à buttiner
def champs(abeilles, pollution, tauxPollen, ressource, maxMiel, minMiel, rsante) :
	if(ressource[0] < maxMiel) :
		if(ressource[0] < minMiel) :
			rsante = dangerMiel(rsante)
		pollution=pollueChamp(*pollution)
		#print("Taux de polution dans les champs : ", pollution)
		tauxPollen=pollenChamp(*tauxPollen)
		#print("Taux de pollen dans les champs : ", tauxPollen)
		ressource, abeilles=envoyerAbeilles(ressource[0], ressource[1], ressource[2], abeilles, pollution, *tauxPollen)
		print("\nAvant conversion, les ressources sont : ", ressource)
		ressource=conversionMiel(*ressource)
		print("Après conversion, les ressources sont : ", ressource)
	else :
		print("Il y a trop de miel dans la ruche, les abeilles n'ont pas envie de buttiner...")
	return(ressource, rsante, abeilles)
