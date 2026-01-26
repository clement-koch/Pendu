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
victory_music_played = False
play_sound_dead = True
player_name = ""

def print_menu():
    screen.blit(menu_background, (0,0))
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

def print_potence() :
    if life < 7 :
        screen.blit(pygame.transform.scale(pygame.image.load(f'assets/images//potence/potence{life}.png'), (350, 260)),(300, 30))

def print_moon() :
    global img_play_background
    if life <= 1 :
        img_play_background = pygame.transform.scale(pygame.image.load('assets/images/fond_jeu_rouge.png'),(1000,750))
        screen.blit(img_red_moon, (105, 20))
    elif life == 2 :
        screen.blit(img_moon2, (105, 20)) 
    elif life <= 4 :
        screen.blit(img_moon1, (122, 20))
    elif life <= 6 :
        screen.blit(img_moon0, (122, 20))
    
def print_keyboard() :
    row = 0
    column = 0
    font = pygame.font.SysFont('Rockwell', 30, bold=True)
    for i in range(len(list_alph)):
        letter = font.render(list_alph[i], 1, (245, 222, 179))
        case = None
        
        if list_alph[i] in list_letter and list_alph[i] in str_word:
            case = img_grenn_case
        elif list_alph[i] in list_letter and list_alph[i] not in str_word:
            case = img_red_case 
        else:
            case = img_case
        if column % 9 == 0:
            row += 1
            column = 0

        x = 250 + (column * 60)
        y = 510 + (row * 60)
        if i < 18:
            screen.blit(case, (x, y))
            screen.blit(letter, (x+15, y+5))
        else:
            screen.blit(case, (x+30, y))
            screen.blit(letter, ((x+15+30), y+5))

        column += 1
    
def print_game():
    pygame.display.get_surface().fill((255,255,255))
    screen.blit(img_play_background, (0,0))
    font = pygame.font.SysFont('Rockwell', 30, bold=True)

    txt_hidden_word = font.render(hidden_word, 1, (0,0,0))

    screen.blit(img_hidden_word, (315, 370))    
    screen.blit(img_btn_exit, (910,0))
    screen.blit(txt_hidden_word, (355, 380))
    print_potence()
    print_moon()
    print_keyboard()


def print_game_over_window(game_status, score=None) :
    global timer, bar_change
    font_title = pygame.font.SysFont('Rockwell', 39, bold=True)
    font = pygame.font.SysFont('Rockwell', 30, bold=True)
    txt_game_status = font_title.render(game_status.upper(), 1, (245, 222, 179))
    screen.blit(pygame.transform.scale(img_sign, (600, 300)), (280, -100))
    screen.blit(txt_game_status, (480, 50))
    if score != None :
        txt_score = font.render(f"Score : {score}", 1, (245, 222, 179))
        screen.blit(txt_score, (490, 110))


    txt_name = font.render("Nom :", 1, (245, 222, 179))
    font = pygame.font.Font(None, 30)
    word_size = font.size(player_name)[0]
    txt_player_name = font.render(player_name, 1, (0,0,0))

    bar = pygame.Rect(480+word_size, 155, 1, 27)
    screen.blit(pygame.transform.scale(pygame.image.load('assets/images/papier.png'), (300, 35)), (470, 150))

    if datetime.now() >= timer + timedelta(seconds=0.5) and writing:
        bar_change = not bar_change
        timer = datetime.now()
    if bar_change:
        pygame.draw.rect(screen, (0, 0, 0), bar)

    screen.blit(img_btn_replay, (800, 60))
    screen.blit(img_btn_add_word, (770, 150))
    screen.blit(txt_player_name, (480, 160))
    screen.blit(txt_name, (360, 150))
    

def music(start):
    if start:
        pygame.mixer.music.load("assets/sons/jeu.mp3")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load("assets/sons/menu.mp3")
        pygame.mixer.music.play(-1)


def valid_letter_sound(valid_letter) :
    if valid_letter :
        pygame.mixer.Sound("assets/sons/ding.mp3").play()
    elif not valid_letter and valid_letter != None :
        pygame.mixer.Sound("assets/sons/marteau2.wav").play()
    return None


def write(word, letter):
    word += letter
    return word

def remove(word):
    global str_word_to_add
    removed_word = ""
    for i in range(len(word)-1):
        removed_word += word[i]
    return removed_word


def print_scores_window(highscores):
    screen.blit(menu_background, (0,0))
    font_title = pygame.font.SysFont('Rockwell', 35, bold=True)
    font_score = pygame.font.SysFont('Rockwell', 25)
    font_small = pygame.font.SysFont('Rockwell', 18)
    
    #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(150, 50, 700, 650))
    screen.blit(score_background, (150, 50))
    txt_title = font_title.render("MEILLEURS SCORES", 1, (0, 0, 0))
    screen.blit(txt_title, (320, 150))
    
    if not highscores:
        txt_empty = font_score.render("Aucun score enregistré", 1, (100, 100, 100))
        screen.blit(txt_empty, (280, 200))
    else:
        y_pos = 200
        for i, score_entry in enumerate(highscores):
            txt_score = font_score.render(f"{i+1}. {score_entry['Nom']} - {score_entry['Score']} pts", 1, (0, 0, 0))
            screen.blit(txt_score, (270, y_pos))
            y_pos += 40
    
    txt_back = font_small.render("Appuyez sur une touche pour revenir", 1, (195, 195, 195))
    screen.blit(txt_back, (330, 630))


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
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print_scores_window(charger_scores())
                pygame.display.flip()
                waiting = True
                while waiting:
                    for wait_event in pygame.event.get():
                        if wait_event.type == pygame.QUIT:
                            waiting = False
                            return True, False, False, False
                        if wait_event.type == pygame.KEYDOWN or wait_event.type == pygame.MOUSEBUTTONDOWN:
                            waiting = False         
    
    return True, False, False, True


#========= Settings ==========#
def settings():
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
                str_word_to_add = remove(str_word_to_add)
            else:
                str_word_to_add = write(str_word_to_add, event.unicode)
    
    return False, False, True, True

#========= Jeu ==========#
def game():
    global list_words, list_letter, hidden_word, life, str_word, victory_music_played, nb_l, writing, player_name, play_sound_dead, img_play_background
    valid_letter = None
    
    if list_words == []:
        list_words = separation(difficulty)
        #print(list_words)
    
    if str_word == "" or str_word == None:
        str_word =choix_mot(list_words)
        print(str_word)
        hidden_word = mot_to_undersocre(str_word)
    
    print_game()
    game_status = verification_victoire(hidden_word, life)

    # fin de partie :
    if game_status != None :
        points = score(life, nb_l, difficulty)
        highscores = charger_scores()
        print_game_over_window(game_status, points)
        #player_name = "test" # à modifier à un input pygame
        if game_status == 'defaite'and play_sound_dead : 
            pygame.mixer.Sound("assets/sons/mort.mp3").play()
            play_sound_dead = False
        elif game_status == 'victoire':
            if not victory_music_played:
                pygame.mixer.music.load("assets/sons/gagne.mp3")
                pygame.mixer.music.play(-1)
                victory_music_played = True

    # commandes :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True, False, False, False
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if btn_exit.collidepoint(event.pos):
                    list_words, hidden_word, str_word, life, game_status,list_letter, nb_l, player_name, play_sound_dead = recommencer(list_words,hidden_word,str_word,life,game_status,list_letter, nb_l, player_name, play_sound_dead)
                    img_play_background = pygame.transform.scale(pygame.image.load('assets/images/fond_jeu.png'),(1000,750))
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
                            if pygame.Rect(250+(column*(50+10)), 510+(row*(50+10)), 50, 50).collidepoint(event.pos) and list_alph[i] not in list_letter:
                                letter = input_lettre(list_alph[i])
                                list_letter.append(letter)
                                hidden_word, life, valid_letter, nb_l = verif_mot(letter,hidden_word,str_word,life, nb_l)
                        else: # derniere ligne du clavier
                            if pygame.Rect(250+30+(column*(50+10)), 510+(row*(50+10)), 50, 50).collidepoint(event.pos) and list_alph[i] not in list_letter:
                                letter = input_lettre(list_alph[i])
                                list_letter.append(letter)
                                hidden_word, life, valid_letter, nb_l = verif_mot(letter,hidden_word,str_word,life, nb_l)
                        column += 1
                elif game_status != None and  player_name_input.collidepoint(event.pos):
                    writing = True
                elif game_status != None and btn_add_score.collidepoint(event.pos) and player_name != "" :
                    pygame.mixer.Sound("assets/sons/clique.wav").play()
                    highscore(points, highscores)
                    ajouter_score(player_name, points, highscores)
                else:
                    if btn_replay.collidepoint(event.pos):
                        pygame.mixer.Sound("assets/sons/clique.wav").play()
                        list_words, hidden_word, str_word, life, game_status,list_letter, nb_l, player_name, play_sound_dead = recommencer(list_words,hidden_word,str_word,life,game_status,list_letter, nb_l, player_name, play_sound_dead)
                        img_play_background = pygame.transform.scale(pygame.image.load('assets/images/fond_jeu.png'),(1000,750))
                        victory_music_played = False
                        music(True)
                    writing = False

        if event.type == pygame.KEYDOWN :
            #racourcie clavier
            if event.unicode.isalpha() and event.unicode not in list_letter and game_status == None:
                letter = input_lettre(event.unicode)
                list_letter.append(letter)
                hidden_word, life, valid_letter, nb_l = verif_mot(letter,hidden_word,str_word,life, nb_l)
            # input name
            elif game_status != None and writing and event.key == 8:
                player_name = remove(player_name)
            elif game_status != None and writing:
                player_name = write(player_name, event.unicode)
        
        # Gestion du clic pour recommencer après victoire/défaite
        #if event.type == pygame.MOUSEBUTTONDOWN and game_status != None:
            #list_words, hidden_word, str_word, life, game_status,list_letter, nb_l = recommencer(list_words,hidden_word,str_word,life,game_status,list_letter, nb_l)
            #victory_music_played = False

        valid_letter = valid_letter_sound(valid_letter)

    
    
    return False, True, False, True

# Initialisation de pygame
pygame.init()
pygame.display.set_caption('Pendu')
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 750))

# Chargement des images
menu_background = pygame.transform.scale(pygame.image.load('assets/images/fond_menu.png'), (1000, 750))
settings_background = pygame.transform.scale(pygame.image.load('assets/images/fond_settings.png'), (1000, 750))
score_background = pygame.transform.scale(pygame.image.load('assets/images/parchemin.png'), (700, 650))
img_play_background = pygame.transform.scale(pygame.image.load('assets/images/fond_jeu.png'),(1000,750))
img_btn_play = pygame.transform.scale(pygame.image.load('assets/images/jouer.png'), (300, 150))
img_btn_settings = pygame.transform.scale(pygame.image.load('assets/images/reglages.png'), (300, 150))
img_sign_settings = pygame.transform.scale(img_btn_settings, (350, 160))
img_btn_quit = pygame.transform.scale(pygame.image.load('assets/images/quitter.png'), (300, 150))
img_btn_exit = pygame.transform.scale(pygame.image.load('assets/images/croix.png'), (80, 80))
img_sign = pygame.transform.scale(pygame.image.load('assets/images/pancarte.png'), (400, 250))
img_btn_add_difficulty = pygame.transform.scale(pygame.image.load('assets/images/+.png'), (50, 40))
img_btn_less_difficulty = pygame.transform.scale(pygame.image.load('assets/images/-.png'), (50, 40))
img_btn_add_word = pygame.transform.scale(pygame.image.load('assets/images/coche.png'), (50, 40))
img_case = pygame.transform.scale(pygame.image.load('assets/images/case.png'), (50, 50))
img_red_case = pygame.transform.scale(pygame.image.load('assets/images/case_rouge.png'), (50, 50))
img_grenn_case = pygame.transform.scale(pygame.image.load('assets/images/case_verte.png'), (50, 50))
img_hidden_word = pygame.transform.scale(pygame.image.load('assets/images/papier.png'), (300, 50))
img_moon2 = pygame.transform.scale(pygame.image.load('assets/images/lune2.png'), (150, 120))
img_moon1 = pygame.transform.scale(pygame.image.load('assets/images/lune1.png'), (120, 105))
img_moon0 = pygame.transform.scale(pygame.image.load('assets/images/lune0.png'), (120, 105))
img_red_moon = pygame.transform.scale(pygame.image.load('assets/images/lune_rouge.png'), (150, 120))
img_btn_replay = pygame.transform.scale(pygame.image.load('assets/images/replay.png'), (50, 49))


# Définition des boutons
btn_start = pygame.Rect(352, 190, 300, 95)
btn_word = pygame.Rect(352, 337, 298, 92)
btn_quit = pygame.Rect(352, 483, 298, 92)
txt_input = pygame.Rect(325, 285, 300, 35)
btn_exit = pygame.Rect(915, 20, 75, 60)
btn_settings = pygame.Rect(625, 283, 50, 40)
btn_add_difficulty = pygame.Rect(600, 510, 50, 40)
btn_less_difficulty = pygame.Rect(350, 510, 50, 40)
player_name_input = pygame.Rect(470, 150, 300, 35)
btn_replay = pygame.Rect(800, 60, 50, 48)
btn_add_score = pygame.Rect(770, 150, 35, 35)

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