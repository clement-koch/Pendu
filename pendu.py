from random import *

def choix_mot (fichier):
    with open (fichier,"r") as f:
        mot=f.readlines()
        nb_ligne=randint(0,len(mot)-1)
        print(mot[nb_ligne])
        return mot[nb_ligne]
     
def mot_to_undersocre(mot):
    underscore=[]
    mot_cache=""
    for i in range (len(mot)-1):
        underscore.append("_")
        underscore.append(" ")
    mot_cache=mot_cache.join(underscore)
    return mot_cache
print(mot_to_undersocre(choix_mot("mots.txt")))