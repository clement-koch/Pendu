import pygame
from datetime import datetime, timedelta
from logic import *

# Variables globales
str_word_to_add = ""
str_word = ""
timer = datetime.now()
bar_change = False
list_alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_letter = []
list_difficulty = ['Facile', 'Normal', 'Difficile']
difficulty = 1
life = 7
hidden_word = '_'
list_words = []
nb_l = 0
writing = False
game_status = None


def print_menu():
    screen.blit(menu_background, (0,0))
    
    font = pygame.font.Font(None, 35)
    txt_start = font.render("Commencer", 1, (255,255,255))
    txt_word = font.render("Ajouter des mots", 1, (255,255,255))
    txt_quit = font.render("Quitter", 1, (255,255,255))
    
    screen.blit(img_btn_play, (350,135))
    screen.blit(img_btn_settings, (350,280))
    screen.blit(img_btn_quit, (350,425))
    
    pygame.display.flip()

def print_settings():
    global timer, bar_change
    screen.blit(settings_background, (0,0))
    screen.blit(img_sign, (300,320))
    screen.blit(img_sign, (300,100))
    screen.blit(img_sign_settings, (325,-30))
    screen.blit(pygame.transform.scale(pygame.image.load('assets/images/papier.png'), (200, 40)), (400, 510))
    screen.blit(img_btn_add_difficulty, (600, 510))
    screen.blit(img_btn_less_difficulty, (350, 510))
    screen.blit(img_btn_add_word, (625, 283))
    
    font = pygame.font.Font(None, 30)
    font_title = pygame.font.SysFont('Rockwell', 39, bold=True)
    txt_difficulty = font_title.render("DIFFICULTÉ", 1, (245, 222, 179))
    txt_var_difficulty = font_title.render(list_difficulty[difficulty], 1, (0, 0, 0))
    word_size = font.size(str_word_to_add)[0]
    txt_add = font_title.render("AJOUTER UN MOT", 1, (245, 222, 179))
    txt_word = font.render(str_word_to_add, 1, (0,0,0))

    bar = pygame.Rect(335+word_size, 290, 1, 27)
    screen.blit(pygame.transform.scale(pygame.image.load('assets/images/papier.png'), (300, 35)), (325, 285))

    if datetime.now() >= timer + timedelta(seconds=0.5) and writing:
        bar_change = not bar_change
        timer = datetime.now()
    if bar_change:
        pygame.draw.rect(screen, (0, 0, 0), bar)

    screen.blit(img_btn_exit, (910,0))
    screen.blit(txt_difficulty, (375, 455))
    screen.blit(txt_var_difficulty, (420, 505))
    screen.blit(txt_word, (335, 295))
    screen.blit(txt_add, (320, 235))

def print_game():
    pygame.display.get_surface().fill((0,0,0))
    font = pygame.font.Font(None, 30)
    rect_hiden_word = pygame.Rect(350, 200, 300, 35)
    txt_hidden_word = font.render(hidden_word, 1, (0,0,0))

    pygame.draw.rect(screen, (255, 255, 255), rect_hiden_word)
    
    screen.blit(img_btn_exit, (910,0))
    screen.blit(txt_hidden_word, (355, 210))

    row = 0
    column = 0
    for i in range(len(list_alph)):
        letter = font.render(list_alph[i], 1, (0,0,0))
        
        if list_alph[i] in list_letter and list_alph[i] in str_word:
            color = (50, 200, 50)
        elif list_alph[i] in list_letter and list_alph[i] not in str_word:
            color = (200, 50, 50)
        else:
            color = (255, 255, 255)
        
        if column % 9 == 0:
            row += 1
            column = 0
        if i < 18:
            pygame.draw.rect(screen, color, pygame.Rect(250+(column*(50+10)), 400+(row*(50+10)), 50, 50))
            screen.blit(letter, (250+(column*(50+10)), 400+(row*(50+10))))
        else:
            pygame.draw.rect(screen, color, pygame.Rect(250+30+(column*(50+10)), 400+(row*(50+10)), 50, 50))
            screen.blit(letter, (250+30+(column*(50+10)), 400+(row*(50+10))))

        column += 1

def print_game_over_window(game_status) :
    font_title = pygame.font.SysFont('Rockwell', 30, bold=True)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(125, 190, 600, 100))
    txt_game_status = font_title.render(game_status, 1, (0, 0, 0))
    screen.blit(txt_game_status, (320, 220))



def music(start):
    if start:
        pygame.mixer.music.load("assets/sons/jeu.mp3")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load("assets/sons/menu.mp3")
        pygame.mixer.music.play(-1)

def write(string):
    global str_word_to_add
    str_word_to_add += string

def remove():
    global str_word_to_add
    removed_word = ""
    for i in range(len(str_word_to_add)-1):
        removed_word += str_word_to_add[i]
    str_word_to_add = removed_word

#======== Menu Principal ========#
def menu():
    global start, settigs_active, running, menu_active
    
    print_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, False, False, False
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if btn_start.collidepoint(event.pos):
                    pygame.mixer.Sound("assets/sons/clique.wav").play()
                    music(True)
                    return False, True, False, True
                
                if btn_word.collidepoint(event.pos):
                    pygame.mixer.Sound("assets/sons/clique.wav").play()
                    return False, False, True, True
                
                if btn_quit.collidepoint(event.pos):
                    pygame.mixer.Sound("assets/sons/clique.wav").play()
                    pygame.quit()
                    return False, False, False, False
    
    return True, False, False, True

#========= Settings ==========#
def settings():
    """Gère la logique du menu des paramètres"""
    global writing, str_word_to_add, difficulty, list_words
    
    print_settings()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, True, False, False
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if txt_input.collidepoint(event.pos):
                    writing = True
                else:
                    writing = False
                
                if btn_exit.collidepoint(event.pos):
                    pygame.mixer.Sound("assets/sons/clique.wav").play()
                    return True, False, False, True
                
                if btn_settings.collidepoint(event.pos):
                    print(str_word_to_add)
                    ajout_mot_difficulte(ajout_mot(str_word_to_add))
                    pygame.mixer.Sound("assets/sons/son_settings.mp3").play()
                
                if btn_add_difficulty.collidepoint(event.pos):
                    difficulty = (difficulty + 1) % 3
                    list_words = []
                    pygame.mixer.Sound("assets/sons/son_settings.mp3").play()
                
                if btn_less_difficulty.collidepoint(event.pos):
                    difficulty = (difficulty - 1) % 3
                    list_words = []
                    pygame.mixer.Sound("assets/sons/son_settings.mp3").play()
        
        if event.type == pygame.KEYDOWN and writing:
            if event.key == 8:
                remove()
            else:
                write(event.unicode)
    
    return False, False, True, True

#========= Jeu ==========#
def game():
    global list_words, list_letter, hidden_word, life, str_word,game_status
    
    if list_words == []:
        list_words = separation(difficulty)
        print(list_words)
    
    if str_word == "" or str_word == None:
        str_word =choix_mot(list_words)
        print(str_word)
        hidden_word = mot_to_undersocre(str_word)
    
    print_game()
    game_status = verification_victoire(hidden_word, life)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True, False, False, False
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if btn_exit.collidepoint(event.pos):
                    pygame.mixer.Sound("assets/sons/clique.wav").play()
                    music(False)
                    return True, False, False, True
                if game_status == None :
                    row = 0
                    column = 0
                    for i in range(len(list_alph)):
                        if column % 9 == 0:
                            row += 1
                            column = 0
                        if i < 18: # 2 premiere lignes du clavier
                            if pygame.Rect(250+(column*(50+10)), 400+(row*(50+10)), 50, 50).collidepoint(event.pos):
                                #print(list_alph[i])
                                #list_letter.append(list_alph[i])
                                letter = input_lettre(list_alph[i])
                                if letter is not None:
                                    list_letter.append(letter)
                                    hidden_word, life = verif_mot(letter,hidden_word,str_word,life)
                        else: # derniere ligne du clavier
                            if pygame.Rect(250+30+(column*(50+10)), 400+(row*(50+10)), 50, 50).collidepoint(event.pos):
                                #print(list_alph[i])
                                #list_letter.append(list_alph[i])
                                letter = input_lettre(list_alph[i])
                                if letter is not None:
                                    list_letter.append(letter)
                                    hidden_word, life = verif_mot(letter,hidden_word,str_word,life)
                        column += 1
        
        if event.type == pygame.KEYDOWN and game_status == None :
            letter = input_lettre(event.unicode)
            list_letter.append(letter)
            hidden_word, life = verif_mot(letter,hidden_word,str_word,life)
        
        # Gestion du clic pour recommencer après victoire/défaite
        if event.type == pygame.MOUSEBUTTONDOWN and game_status != None:
            list_words, hidden_word, str_word, life, game_status,list_letter = recommencer(list_words,hidden_word,str_word,life,game_status,list_letter)
    
    if game_status == 'defaite':
        pygame.mixer.Sound("assets/sons/mort.mp3").play()
        print_game_over_window(game_status)
        points = score(life, nb_l, difficulty)
        highscores = charger_scores()
        player_name = "test" # à modifier à un input pygame
        highscore(points, highscores)
        ajouter_score(player_name, points, highscores)
        afficher_score()
    elif game_status == 'victoire':       
        print_game_over_window(game_status)
        print("") 
    
    return False, True, False, True

# Initialisation de pygame
pygame.init()
pygame.display.set_caption('Pendu')
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 750))

# Chargement des images
menu_background = pygame.transform.scale(pygame.image.load('assets/images/fond_menu.png'), (1000, 750))
settings_background = pygame.transform.scale(pygame.image.load('assets/images/fond_settings.png'), (1000, 750))
img_btn_play = pygame.transform.scale(pygame.image.load('assets/images/jouer.png'), (300, 150))
img_btn_settings = pygame.transform.scale(pygame.image.load('assets/images/reglages.png'), (300, 150))
img_sign_settings = pygame.transform.scale(img_btn_settings, (350, 160))
img_btn_quit = pygame.transform.scale(pygame.image.load('assets/images/quitter.png'), (300, 150))
img_btn_exit = pygame.transform.scale(pygame.image.load('assets/images/croix.png'), (80, 80))
img_sign = pygame.transform.scale(pygame.image.load('assets/images/pancarte.png'), (400, 250))
img_btn_add_difficulty = pygame.transform.scale(pygame.image.load('assets/images/+.png'), (50, 40))
img_btn_less_difficulty = pygame.transform.scale(pygame.image.load('assets/images/-.png'), (50, 40))
img_btn_add_word = pygame.transform.scale(pygame.image.load('assets/images/coche.png'), (50, 40))

# Définition des boutons
btn_start = pygame.Rect(352, 190, 300, 95)
btn_word = pygame.Rect(352, 337, 298, 92)
btn_quit = pygame.Rect(352, 483, 298, 92)
txt_input = pygame.Rect(325, 285, 300, 35)
btn_exit = pygame.Rect(915, 20, 75, 60)
btn_settings = pygame.Rect(625, 283, 50, 40)
btn_add_difficulty = pygame.Rect(600, 510, 50, 40)
btn_less_difficulty = pygame.Rect(350, 510, 50, 40)

# Variables d'état
running = True
menu_active = True
start = False
settigs_active = False

music(False)

# Boucle principale
while running:
    pygame.display.flip()
    
    if menu_active:
        menu_active, start, settigs_active, running = menu()
    
    elif settigs_active:
        menu_active, start, settigs_active, running = settings()
    
    elif start:
        menu_active, start, settigs_active, running = game()

pygame.quit()