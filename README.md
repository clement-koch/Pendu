#  Jeu du Pendu

Un jeu du pendu interactif développé en Python avec Pygame, offrant une expérience visuelle immersive avec plusieurs niveaux de difficulté.


##  Description

Ce jeu du pendu propose une interface graphique complète avec :
- Trois niveaux de difficulté (Facile, Normal, Difficile)
- Un système de scoring avec tableau des meilleurs scores
- La possibilité d'ajouter vos propres mots
- Des effets sonores et musicaux immersifs
- Une interface graphique thématique avec animations visuelles

<img width="325" height="970" alt="menu_pendu" src="https://github.com/user-attachments/assets/c978e390-f337-4a57-b2fd-12a75d0a71eb" />
<img width="325" height="968" alt="jeu_pendu" src="https://github.com/user-attachments/assets/185f3992-1ef1-4ff5-b332-90712fc76559" />
<img width="325" height="972" alt="reglage_pendu" src="https://github.com/user-attachments/assets/e1174ed5-fd2b-4ee7-8287-831762348f36" />

##  Fonctionnalités

### Menu principal
- **Jouer** : Lance une partie
- **Réglages** : Permet de modifier la difficulté et d'ajouter des mots personnalisés
- **Quitter** : Ferme le jeu
- **Scores** : Appuyez sur `S` pour afficher le tableau des meilleurs scores

### Gameplay
- **7 vies** pour deviner le mot
- **Clavier visuel** interactif avec indication des lettres correctes (vert) et incorrectes (rouge)
- **Raccourcis clavier** : Tapez directement les lettres sur votre clavier
- **Ambiance dynamique** : La lune et le fond changent selon vos vies restantes
- **Système de points** basé sur les vies restantes, le nombre de lettres trouvées et la difficulté

### Paramètres
- Sélection de la difficulté (détermine la longueur des mots)
- Ajout de mots personnalisés au dictionnaire
- Les mots sont automatiquement classés selon leur longueur

##  Prérequis

- Python 3.x
- Pygame

##  Installation

1. Clonez ou téléchargez le projet

2. Installez Pygame :
```bash
pip install pygame
```

3. Assurez-vous que la structure des fichiers est correcte :
```
projet/
│
├── main.py
├── logic.py
├── mots.txt
├── scores.txt (créé automatiquement)
│
└── assets/
    ├── images/
    │   ├── fond_menu.png
    │   ├── fond_jeu.png
    │   ├── fond_settings.png
    │   ├── potence/
    │   │   ├── potence0.png
    │   │   ├── potence1.png
    │   │   └── ...
    │   └── ...
    │
    └── sons/
        ├── menu.mp3
        ├── jeu.mp3
        ├── gagne.mp3
        ├── mort.mp3
        └── ...
```

##  Lancement du jeu

```bash
python main.py
```

##  Comment jouer

1. Lancez le jeu et cliquez sur **"Jouer"**
2. Devinez le mot en cliquant sur les lettres du clavier virtuel ou en utilisant votre clavier
3. Vous disposez de **7 vies** pour trouver le mot
4. À la fin de la partie, entrez votre nom pour enregistrer votre score
5. Consultez le tableau des scores en appuyant sur `S` dans le menu principal

##  Système de scoring

Le score est calculé selon :
- **Nombre de lettres trouvées** : 5 points par lettre
- **Vies restantes** : Bonus allant de 0 à 100 points
- **Multiplicateur de difficulté** :
  - Facile : ×1
  - Normal : ×1.5
  - Difficile : ×2

##  Format du fichier mots.txt

Le fichier `mots.txt` doit être organisé en trois sections séparées par des lignes vides :
```
mot_facile_1
mot_facile_2

mot_normal_1
mot_normal_2

mot_difficile_1
mot_difficile_2
```

##  Caractéristiques techniques

- Gestion des accents et caractères spéciaux (é, è, ê, ç, etc.)
- Sauvegarde automatique des scores en JSON
- Interface responsive avec détection de collision précise
- Système d'animation pour les barres de saisie
- Gestion complète des événements Pygame

##  Résolution de problèmes

- **Le jeu ne se lance pas** : Vérifiez que Pygame est bien installé
- **Images manquantes** : Assurez-vous que tous les assets sont dans le bon dossier
- **Pas de son** : Vérifiez que les fichiers audio sont présents et au bon format

##  Licence

Projet éducatif réalisé dans le cadre d'un apprentissage de la programmation Python et Pygame.

##  Autheurs

- Clément Koch
- Mohamed Mahamoud
- Logann Grange
