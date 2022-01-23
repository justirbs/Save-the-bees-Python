#variables de départ

jour = 1 # jour actuel
maxplaces = 15000 # nombre de places maximum dans la ruche
argent = 0 # quantité d'argent que l'utilisateur possède
miel = 10.0 # quantité de miel que l'utilisateur possède
rsante = 100 # santé de la ruche
nbAb1=10001 # nombre d'abeilles total en début de journée
nbAb2=1 # nombre d'abeilles total en fin de journée
nvIA = 0 # niveau d'IA que possède l'utilisateur
maxMiel = 50 #quantité de miel à partir de laquelle les abeilles ne veulent plus buttiner
minMiel = 10 #quantité de miel en dessous de laquelle les abeilles peuvent être en mauvaise santé

tauxPollen = (0,0,0) #chaque valeur correspond à un champ
pollution = (0,0,0)	 #chaque valeur correspond à un champ
ressource = (miel, 0, argent) #ressources du joueur : miel (en kg), qte de pollen, argent
abeilleEnvoyee = (0,0,0)


#température de base = température idéale pour limiter les pertes au début
temperature = 35
variation = 1

# Dans la liste on a :
reine = 1
abeilleMale = 500
abeilleBat = 2000
abeilleBut = 5000
abeilleVent = 2000
abeilleGard = 500

abeilles = [reine, abeilleMale, abeilleBat, abeilleBut, abeilleVent, abeilleGard]

#on pourra diminuer le taux de reproduction en fonction de la difficulté
tauxReproduction = 2

#on pourra augmenter les dégats des attaques de frelons en fonction de la difficulté
tauxFrelons = 0.1

#on pourra augmenter les dégats des tempêtes en fonction de la difficulté
tauxTempete = 0.3

#on pourra augmenter les dégats des invasions de varroa en fonction de la difficulté
tauxVarroa = 0.3
