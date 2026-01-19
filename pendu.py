def verif_mot(lettre,mot_cache,mot_a_trouver,vie):
    if lettre in mot_a_trouver:
        for i in range(len(mot_a_trouver)):
            if mot_a_trouver[i] == lettre:
                mot_cache[i] = lettre
        return mot_cache, vie
    else:
        vie -= 1
        return mot_cache, vie
    
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
    with open("scores.txt","a") as f:
        f.write(f"{nom_joueur} : {points} points\n")
    return points