#-*- coding: utf-8 -*-

from random import *

import pygame


def choix_mot (fichier):
    with open (fichier,"r", encoding="utf-8") as f:
        mot=f.readlines()
        nb_ligne=randint(0,len(mot)-1)
        print(mot[nb_ligne])
        return mot[nb_ligne].strip().lower()
     
def mot_to_undersocre(mot):
    underscore=[]
    mot_cache=""
    for i in range (len(mot)):
        underscore.append("_")
        underscore.append(" ")
    mot_cache="".join(underscore)
    return mot_cache

def verif_mot(lettre,mot_cache,mot_a_trouver,vie):
    mot_a_trouver_list=list(mot_a_trouver)  
    if lettre in mot_a_trouver:
        mot_cache_list = list(mot_cache)
        for i in range(len(mot_a_trouver)):
            if lettre=="e" and (mot_a_trouver_list[i]=="é" or mot_a_trouver_list[i]=="è" or mot_a_trouver_list[i]=="ê"):
                mot_cache_list[2*i] = lettre
            elif lettre=="é" and (mot_a_trouver_list[i]=="e" or mot_a_trouver_list[i]=="è" or mot_a_trouver_list[i]=="ê"):
                mot_cache_list[2*i] = lettre
            elif lettre == "è" and (mot_a_trouver_list[i]=="e" or mot_a_trouver_list[i]=="é" or mot_a_trouver_list[i]=="ê"):
                mot_cache_list[2*i] = lettre
            elif lettre == "c" and mot_a_trouver_list[i]=="ç":
                mot_cache_list[2*i] = "ç"
            elif lettre == "u" and mot_a_trouver_list[i]=="ù":
                mot_cache_list[2*i] = "ù"
            elif lettre == "a" and (mot_a_trouver_list[i]=="à" or mot_a_trouver_list[i]=="â"):
                mot_cache_list[2*i] = mot_a_trouver_list[i]        
            if mot_a_trouver_list[i] == lettre:
                mot_cache_list[2*i] = lettre
        mot_cache = "".join(mot_cache_list)
        return mot_cache, vie
    else:
        vie -= 1
        return mot_cache, vie
    
def ajout_mot():
    with open("mots.txt","r", encoding="utf-8") as f:
        nouveau_mot = input("Entrez le mot que vous souhaitez ajouter : ").strip().lower()
        #nouveau_mot = pygame.key.start_text_input()
        liste_mots=f.readlines()
        for mot in liste_mots:
            if nouveau_mot == mot.strip().lower():
                print("Le mot existe déjà dans la liste.")
                return ajout_mot()
        if verif_ajout(nouveau_mot) != "Mot valide." :
            return ajout_mot()
        else:
           return nouveau_mot
    
def verification_victoire(mot_cache,vie):
    if vie == 0:
        return "defaite"
    elif "_" not in mot_cache:
        return "victoire"
    
def score(vie,nom_joueur):
    match vie:
        case 7:
            points = 100
        case 6:
            points = 70
        case 5:
            points = 60
        case 4:
            points = 50
        case 3:
            points = 20
        case 2:
            points = 10
        case 1:
            points = 1
        case _:
            points = 0    
    with open("scores.txt","a", encoding="utf-8") as f:
        f.write(f"{nom_joueur} : {points} points\n")
    return points

def input_lettre():
    lettre = input("Entrez une lettre : ").lower()
    if len(lettre) != 1 or not lettre.isalpha():
        print("Veuillez entrer une seule lettre valide.")
        return input_lettre()
    return lettre

def verif_ajout(mot):
    if not mot.isalpha():
        return "Le mot ne doit contenir que des lettres."
    else:
        return "Mot valide."
    
def jeu():
    mot=choix_mot("mots.txt")
    mot_cache=mot_to_undersocre(mot)
    vie=7
    victoire=None
    ajout_mot()
    while victoire is None:
        print(mot_cache)
        print(f"Il vous reste {vie} vies.")
        lettre=input_lettre()
        mot_cache, vie=verif_mot(lettre,mot_cache,mot,vie)
        victoire=verification_victoire(mot_cache,vie)
        if victoire is not None:
            if victoire == "victoire":
                print(f"Félicitations ! Vous avez trouvé le mot : {mot}")
            else:
                print(f"Dommage ! Vous avez perdu. Le mot était : {mot}")
            nom_joueur = input("Entrez votre nom pour enregistrer votre score : ")
            points = score(vie, nom_joueur)
            print(f"Votre score est de {points} points.")
            afficher_score()

def afficher_score(score_file="scores.txt"):
    try:
        with open(score_file, "r", encoding="utf-8") as f:
            scores = f.readlines()
            print("\nScores des joueurs :")
            for ligne in scores:
                print(ligne.strip())
    except FileNotFoundError:
        print("Aucun score enregistré pour le moment.")

if __name__ == "__main__":
    jeu()            