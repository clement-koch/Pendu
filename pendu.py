from random import *

def separation(nv):
    #séparation des niveaux de difficultés
    with open("mots.txt", "r") as f:
        lst_1=[]
        lst_2=[]
        lst_3=[]
        indice=0
        lst_indice=[]
        lst_mot=f.readlines()
        for mot in lst_mot:
            indice+=1
            if mot=="\n":
                lst_indice.append(indice)
        if nv==1:
            for i in range(0,lst_indice[0]-1):
                lst_1.append(lst_mot[i])
            return lst_1
        elif nv==2:
            for j in range(lst_indice[0]+1,lst_indice[1]-1):
                lst_2.append(lst_mot[j])
            return lst_2
        elif nv==3:
            for h in range (lst_indice[1]+1,len(lst_mot)):
                lst_3.append(lst_mot[h])
            return lst_3

def niveau ():
    global nv
    #interogation utilisateur
    lst_nv=[1,2,3]
    nv=int(input("Niveau 1, 2 ou 3? "))
    if nv not in lst_nv:
        return niveau()   
    match nv:
        case 1:           
            return separation(1)
        case 2:
            return separation(2)
        case 3:
            return separation(3)

def choix_mot (liste):
    nb_ligne=randint(0,len(liste)-1)
    mot_a_trouver=liste[nb_ligne]
    print(mot_a_trouver)
    return mot_a_trouver

def mot_to_undersocre(mot):
    underscore=[]
    for i in range (len(mot)-1):
        underscore.append("_")
        underscore.append(" ")
    mot_cache="".join(underscore)
    return mot_cache


print(mot_to_undersocre(choix_mot(niveau())))
