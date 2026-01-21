#-*- coding: utf-8 -*-

from random import *
import json



nb_l=0
list_lettres=[]
max_scores=10

def separation(nv):
    #séparation des niveaux de difficultés
    with open("mots.txt", "r",encoding="utf-8") as f:
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
    mot_a_trouver=liste[nb_ligne].lower().strip()
    print(mot_a_trouver)
    return mot_a_trouver
     
def mot_to_undersocre(mot):
    underscore=[]
    mot_cache=""
    for i in range (len(mot)):
        underscore.append("_")
        underscore.append(" ")
    mot_cache="".join(underscore)
    return mot_cache

def ajout_mot_difficulte(nv_mot):
    
    nb_caractere=len(nv_mot)
    print(nb_caractere)

    if nb_caractere<=7:
        nv=1
    elif nb_caractere<=10:
        nv=2
    else:
        nv=3
    print(nv)
    with open ("mots.txt","r",encoding="utf-8") as f:
        lignes=f.readlines()

    indice_insertion=None
    compteur_separateur=0
    for i, ligne in enumerate(lignes):
        if ligne.strip()=="":
            compteur_separateur+=1
            if  compteur_separateur==nv:
                indice_insertion=i
                break

    if indice_insertion is None:
        indice_insertion=len(lignes)
    
    lignes.insert(indice_insertion,nv_mot+"\n")

    with open("mots.txt","w",encoding="utf-8") as f:
        f.writelines(lignes)
    print(indice_insertion)

def verif_mot(lettre,mot_cache,mot_a_trouver,vie):
    global nb_l
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
        nb_l+=1
        return mot_cache, vie
    else:
        vie -= 1
        return mot_cache, vie
    
def ajout_mot():
    with open("mots.txt","r", encoding="utf-8") as f:
        liste_mots=f.readlines()   
    nouveau_mot = input("Entrez le mot que vous souhaitez ajouter : ").strip().lower()
    
    for mot in liste_mots:
        if nouveau_mot == mot.strip().lower():
            print("Le mot existe déjà dans la liste.")
            return ajout_mot()
    
    if verif_ajout(nouveau_mot) != "Mot valide.":
        return ajout_mot()
    else:
        return nouveau_mot
    
def verification_victoire(mot_cache,vie):
    if vie == 0:
        return "defaite"
    elif "_" not in mot_cache:
        return "victoire"
    
def score(vie,nb_l):
    global nv
    points = 0
    if nb_l > 0:
        points += (nb_l * 5)
    match vie:
        case 7:
            points += 100
        case 6:
            points += 70
        case 5:
            points += 60
        case 4:
            points += 50
        case 3:
            points += 20
        case 2:
            points += 10
        case 1:
            points += 1
        case _:
            points += 0 
    match nv:
        case 1:
            points *=1
        case 2:
            points *=1.5
        case 3:
            points *=2
    return points

def sauvegarder_score(highscores, score_file="scores.txt"):
    with open(score_file, "w", encoding="utf-8") as f:
        json.dump(highscores, f, ensure_ascii=False, indent=4)

def highscore(score,highscores):
    if len(highscores) < max_scores:
        return True
    else: 
        return score > highscores[-1]["Score"]
def ajouter_score(nom_joueur, points,highscores):
    nouveau_score = {"Nom": nom_joueur, "Score": points}
    highscores.append(nouveau_score)
    highscores.sort(key=lambda x: x["Score"], reverse=True)
    if len(highscores) > max_scores:
        highscores.pop()
    sauvegarder_score(highscores)

def input_lettre():
    global list_lettres
    lettre = input("Entrez une lettre : ").lower()
    if len(lettre) != 1 or not lettre.isalpha():
        print("Veuillez entrer une seule lettre valide.")
        return input_lettre()
    elif lettre in list_lettres:
        print("Vous avez déjà essayé cette lettre. Choisissez-en une autre.")
        return input_lettre()
    list_lettres.append(lettre)
    return lettre

def verif_ajout(mot):
    if not mot.isalpha():
        return "Le mot ne doit contenir que des lettres."
    else:
        return "Mot valide."
    
def jeu():
    global list_lettres
    list_lettres = []
    liste = niveau()  # niveau() retourne déjà la liste des mots pour le niveau choisi
    mot=choix_mot(liste)
    mot_cache=mot_to_undersocre(mot)
    vie=7
    victoire=None
    nv_mot=ajout_mot()
    ajout_mot_difficulte(nv_mot)
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
            points = score(vie, nb_l)
            print(f"Votre score est de {points} points.")
            highscores = charger_scores()
            highscore(points, highscores)
            ajouter_score(nom_joueur, points, highscores)
            afficher_score()

def charger_scores(score_file="scores.txt"):
    try:
        with open(score_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            f.seek(0)
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def afficher_score(score_file="scores.txt"):
    try:
        with open(score_file, "r", encoding="utf-8") as f:
            scores = json.load(f)
            print("\nScores des joueurs :")
            for ligne,score in enumerate(scores, start=1):
                print(f"{ligne}. {score['Nom']} - {score['Score']}")
    except FileNotFoundError:
        print("Aucun score enregistré pour le moment.")

def main():
    jeu()

if __name__ == "__main__":
    main()    