import pygame
from datetime import datetime, timedelta

str_word = ""
timer = datetime.now()
bar_change = False
list_alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def print_menu() :
    screen.blit(menu_backround, (0,0))

    #ecriture
    font=pygame.font.Font(None, 35)
    txt_start = font.render("Commencer",1,(255,255,255))
    txt_word = font.render("Ajouter des mots", 1, (255,255,255))
    txt_quit = font.render("Quitter", 1, (255,255,255))
    
    # Bouton Start :
    pygame.draw.rect(screen, (100, 200, 50), btn_start)
    screen.blit(txt_start, (420, 200))
    #Bouton Word :
    pygame.draw.rect(screen, (50, 50, 200), btn_word)
    screen.blit(txt_word, (400, 375))
    # Bouton Quit :
    pygame.draw.rect(screen, (150, 50, 50), btn_quit)
    screen.blit(txt_quit, (450, 525))
    
    pygame.display.flip()

def print_add_word() :
    global timer, bar_change
    pygame.display.get_surface().fill((0,0,0)) # à modifier par l'image de fond
    
    #ecriture
    font=pygame.font.Font(None, 30)
    #str_word = ""
    word_size = font.size(str_word)[0]
    txt_add = font.render("Ajouter",1,(255,255,255))
    txt_word = font.render(str_word,1,(0,0,0))

    bar = pygame.Rect(355+word_size, 205, 1, 27)

    pygame.draw.rect(screen, (255, 255, 255), txt_input)
    pygame.draw.rect(screen, (20, 0, 120), pygame.Rect(410, 250, 150, 50))

    # clignotement de la barre
    if datetime.now() >= timer + timedelta(seconds=0.5) and writing:
        bar_change = not bar_change
        timer = datetime.now()

    if bar_change:
        pygame.draw.rect(screen, (0, 0, 0), bar)
    else:
        pygame.draw.rect(screen, (255, 255, 255), bar)

    screen.blit(txt_word, (355, 210))
    screen.blit(txt_add, (450, 265))

def print_game() :
    str_hidden_word = "___________"
    
    pygame.display.get_surface().fill((0,0,0)) # à modifier par l'image de fond
    font=pygame.font.Font(None, 30)
    rect_hiden_word = pygame.Rect(350, 200, 300, 35)
    txt_hidden_word = font.render(str_hidden_word,1,(0,0,0))

    pygame.draw.rect(screen, (255, 255, 255), rect_hiden_word)
    pygame.draw.rect(screen, (150, 80, 20), btn_exit_game)
    screen.blit(txt_hidden_word, (355, 210))

    row = 0
    column = 0
    for i in range(len(list_alph)) :
        if column % 9 == 0 :
            row += 1
            column = 0
        if i < 18 :
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(250+(column*(50+10)), 400+(row*(50+10)), 50, 50))
        else : 
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(250+ 30 +(column*(50+10)), 400+(row*(50+10)), 50, 50))

        column += 1


def game() :
    for i in list_alph :
        print()


def write(string) :
    global str_word
    str_word += string

def remove() :
    global str_word
    removed_word = ""

    for i in range(len(str_word)-1) :
        removed_word += str_word[i]
    str_word = removed_word



#initialisation de pygame
pygame.init()
pygame.display.set_caption('Pendu')
#pygame.mixer.init()

screen = pygame.display.set_mode((1000, 750))

menu_backround = pygame.transform.scale(pygame.image.load('assets/images/fond_menu.png'), (1000, 750))

#def des Boutons :
btn_start = pygame.Rect(350, 175, 300, 75)
btn_word = pygame.Rect(350, 350, 300, 75)
btn_quit = pygame.Rect(350, 500, 300, 75)
txt_input = pygame.Rect(350, 200, 300, 35)
btn_exit_game = pygame.Rect(960, 5, 35, 35)

running = True
menu = True
game = False
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
                        game = True
                        menu = False

                    if btn_word.collidepoint(event.pos) :
                        menu = False
                        add_word = True

                    if btn_quit.collidepoint(event.pos) :
                        running = False
                        menu = False
                        pygame.quit()

    if add_word :
        print_add_word()

        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1: # 1= clique gauche
                    if txt_input.collidepoint(event.pos) :
                        writing = True
                    else :
                        writing = False
            if event.type == pygame.KEYDOWN and writing :
                if event.key == 8 :
                    remove()
                else :
                    write(event.unicode)
    if game :
        print_game()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1: # 1= clique gauche
                    if btn_exit_game.collidepoint(event.pos) :
                        game = False
                        menu = True

                
    if event.type == pygame.QUIT:
            running = False
            menu = False
            pygame.quit()