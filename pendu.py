import pygame
from datetime import datetime, timedelta

str_word_to_add = ""
str_word = "test"
timer = datetime.now()
bar_change = False
list_alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_letter = []
list_difficulty = ['Facile', 'Normal', 'Difficile']
difficulty = 2

def print_menu() :
    screen.blit(menu_background, (0,0))

    #ecriture
    font=pygame.font.Font(None, 35)
    txt_start = font.render("Commencer",1,(255,255,255))
    txt_word = font.render("Ajouter des mots", 1, (255,255,255))
    txt_quit = font.render("Quitter", 1, (255,255,255))
    
    # Bouton Start :
    #pygame.draw.rect(screen, (100, 200, 50), btn_start)
    #screen.blit(txt_start, (420, 200))
    screen.blit(img_btn_play, (350,135))
    #Bouton Word :
    #pygame.draw.rect(screen, (50, 50, 200), btn_word)
    #screen.blit(txt_word, (400, 375))
    screen.blit(img_btn_settings, (350,280))
    # Bouton Quit :
    #pygame.draw.rect(screen, (150, 50, 50), btn_quit)
    #screen.blit(txt_quit, (450, 525))
    screen.blit(img_btn_quit, (350,425))
    
    pygame.display.flip()

def print_settings() :
    global timer, bar_change
    screen.blit(settings_background, (0,0))
    screen.blit(img_btn_settings, (350,-20))
    screen.blit(img_sign, (300,320))
    screen.blit(img_sign, (300,100))
    screen.blit(pygame.transform.scale(pygame.image.load('assets/images/papier.png'), (200, 40)), (400, 510))
    screen.blit(img_btn_add_difficulty, (600, 510))
    screen.blit(img_btn_less_difficulty, (350, 510))
    screen.blit(img_btn_add_word, (625, 283))

    
    #ecriture
    font=pygame.font.Font(None, 30)
    font_title = pygame.font.SysFont('Rockwell', 39, bold=True)
    txt_difficulty = font_title.render("DIFFICULTÉ",1,(245, 222, 179))
    txt_var_difficulty = font_title.render(list_difficulty[difficulty],1,(0, 0, 0))
    word_size = font.size(str_word_to_add)[0]
    txt_add = font_title.render("AJOUTER UN MOT",1,(245, 222, 179))
    txt_word = font.render(str_word_to_add,1,(0,0,0))

    bar = pygame.Rect(335+word_size, 290, 1, 27)

    screen.blit(pygame.transform.scale(pygame.image.load('assets/images/papier.png'), (300, 35)), (325, 285))
    #pygame.draw.rect(screen, (20, 0, 120), pygame.Rect(635, 285, 35, 35))

    # clignotement de la barre du texte
    if datetime.now() >= timer + timedelta(seconds=0.5) and writing:
        bar_change = not bar_change
        timer = datetime.now()

    if bar_change:
        pygame.draw.rect(screen, (0, 0, 0), bar)
    

    #pygame.draw.rect(screen, (150, 80, 20), btn_exit)
    screen.blit(img_btn_exit, (910,0))
    screen.blit(txt_difficulty, (375, 455))
    screen.blit(txt_var_difficulty, (420, 505))
    screen.blit(txt_word, (335, 295))
    screen.blit(txt_add, (320, 235))


def print_game() :
    str_hidden_word = "___________"

    pygame.display.get_surface().fill((0,0,0)) # à modifier par l'image de fond
    font=pygame.font.Font(None, 30)
    rect_hiden_word = pygame.Rect(350, 200, 300, 35)
    txt_hidden_word = font.render(str_hidden_word,1,(0,0,0))

    pygame.draw.rect(screen, (255, 255, 255), rect_hiden_word)
    #pygame.draw.rect(screen, (150, 80, 20), btn_exit)
    
    screen.blit(img_btn_exit, (910,0))
    screen.blit(txt_hidden_word, (355, 210))

    row = 0
    column = 0
    for i in range(len(list_alph)) :
        letter = font.render(list_alph[i],1,(0,0,0))
        # couleur 
        if list_alph[i] in list_letter and list_alph[i] in str_word :
            color = (50, 200, 50)
        elif list_alph[i] in list_letter and list_alph[i] not in str_word :
            color = (200, 50, 50)
        else :
            color = (255, 255, 255)
        # placement
        if column % 9 == 0 :
            row += 1
            column = 0
        if i < 18 :
            pygame.draw.rect(screen, color, pygame.Rect(250+(column*(50+10)), 400+(row*(50+10)), 50, 50))
            screen.blit(letter, (250+(column*(50+10)), 400+(row*(50+10))))
        else : 
            pygame.draw.rect(screen, color, pygame.Rect(250+ 30 +(column*(50+10)), 400+(row*(50+10)), 50, 50))
            screen.blit(letter, (250+ 30 +(column*(50+10)), 400+(row*(50+10))))

        column += 1


def game() :
    for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1: # 1= clique gauche
                    row = 0
                    column = 0
                    for i in range(len(list_alph)) :
                        if column % 9 == 0 :
                            row += 1
                            column = 0
                        if pygame.Rect(250+(column*(50+10)), 400+(row*(50+10)), 50, 50).collidepoint(event.pos) :
                            print(list_alph[i])
                    column += 1
                        

def write(string) :
    global str_word_to_add
    str_word_to_add += string

def remove() :
    global str_word_to_add
    removed_word = ""

    for i in range(len(str_word_to_add)-1) :
        removed_word += str_word_to_add[i]
    str_word_to_add = removed_word


#initialisation de pygame
pygame.init()
pygame.display.set_caption('Pendu')
#pygame.mixer.init()

screen = pygame.display.set_mode((1000, 750))

menu_background = pygame.transform.scale(pygame.image.load('assets/images/fond_menu.png'), (1000, 750))
settings_background = pygame.transform.scale(pygame.image.load('assets/images/fond_settings.png'), (1000, 750))
img_btn_play = pygame.transform.scale(pygame.image.load('assets/images/jouer.png'), (300, 150))
img_btn_settings = pygame.transform.scale(pygame.image.load('assets/images/reglages.png'), (300, 150))
img_btn_quit = pygame.transform.scale(pygame.image.load('assets/images/quitter.png'), (300, 150))
img_btn_exit = pygame.transform.scale(pygame.image.load('assets/images/croix.png'), (80, 80))
img_sign = pygame.transform.scale(pygame.image.load('assets/images/pancarte.png'), (400, 250))
img_btn_add_difficulty = pygame.transform.scale(pygame.image.load('assets/images/+.png'), (50, 40)) 
img_btn_less_difficulty = pygame.transform.scale(pygame.image.load('assets/images/-.png'), (50, 40))
img_btn_add_word = pygame.transform.scale(pygame.image.load('assets/images/coche.png'), (50, 40))


# def des Boutons :
    # menu principale
btn_start = pygame.Rect(352, 190, 300, 95)
btn_word = pygame.Rect(352, 337, 298, 92)
btn_quit = pygame.Rect(352, 483, 298, 92)
    # menu settings
txt_input = pygame.Rect(325, 285, 300, 35)
btn_exit = pygame.Rect(915, 20, 75, 60)
btn_add_word = pygame.Rect(625, 283, 50, 40)
btn_add_difficulty = pygame.Rect(600, 510, 50, 40)
btn_less_difficulty = pygame.Rect(350, 510, 50, 40)

running = True
menu = True
start = False
add_word = False
writing = False

while running :
    pygame.display.flip()
    #======== Menu Principal =========#
    if menu :
        print_menu()

        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1: # 1= clique gauche
                    if btn_start.collidepoint(event.pos) :
                        start = True
                        menu = False

                    if btn_word.collidepoint(event.pos) :
                        menu = False
                        add_word = True

                    if btn_quit.collidepoint(event.pos) :
                        running = False
                        menu = False
                        pygame.quit()

    if add_word :
        print_settings()

        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1: # 1= clique gauche
                    if txt_input.collidepoint(event.pos) :
                        writing = True
                    else :
                        writing = False
                if btn_exit.collidepoint(event.pos) :
                        add_word = False
                        menu = True
                if btn_add_word.collidepoint(event.pos) :
                    print(str_word_to_add) # à remplacer par la fonction qui ajoute le mot
                if btn_add_difficulty.collidepoint(event.pos) :
                    difficulty = (difficulty + 1) % 3
                if btn_less_difficulty.collidepoint(event.pos) :
                    difficulty = (difficulty - 1) % 3

            if event.type == pygame.KEYDOWN and writing :
                if event.key == 8 :
                    remove()
                else :
                    write(event.unicode)

    if start :
        print_game()
        #game()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1: # 1= clique gauche
                    if btn_exit.collidepoint(event.pos) :
                        start = False
                        menu = True

                    row = 0
                    column = 0
                    for i in range(len(list_alph)) :
                        if column % 9 == 0 :
                            row += 1
                            column = 0
                        if i < 18 :
                            if pygame.Rect(250+(column*(50+10)), 400+(row*(50+10)), 50, 50).collidepoint(event.pos) :
                                print(list_alph[i])
                                list_letter.append(list_alph[i])
                        else : 
                            if pygame.Rect(250+ 30 +(column*(50+10)), 400+(row*(50+10)), 50, 50).collidepoint(event.pos) :
                                print(list_alph[i])
                                list_letter.append(list_alph[i])

                        column += 1
            if event.type == pygame.KEYDOWN :
                list_letter.append(event.unicode) # à modifier par la fonction correspondante

                
    if event.type == pygame.QUIT:
            running = False
            menu = False
            pygame.quit()