import pygame, sys, time, random
from pygame.locals import *

#tamanho da tela e o nome do jogo
def game_init(w,h):
    pygame.init()
    #tamanho da tela
    width,height = w,h
    size = width,height
    #modo do display do pygame
    display = pygame.display.set_mode(size)
    #nome do projeto
    pygame.display.set_caption("Ping Pong")
    return display

width,height = 640, 480
display = game_init(width,height)
#para por na cor da tela
display_window = pygame.display.set_mode((width, height))

#clock ?
fps = 25

#tempo
sec = 0
t = pygame.time.get_ticks()
clock = pygame.time.Clock()

#cores
green = (0,200,200)
black = (0, 0, 0)
white = (255, 255, 255)

#tempo - fonte e cor
font = pygame.font.Font(None,30)
text_color = green

#posicao inicial do retangulo
rect_x = 272
rect_y = 470

#controle
floor_collision = False
win = False

# bola - cor, mudanca, coordenadas
x_cor = random.randint(15, width - 15)
y_cor = random.randint(15, height - 15)

x_change = random.randint(3, 7)
y_change = random.randint(3, 7)

coordinates = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    key = pygame.key.get_pressed()

    #tempo - jogando
    if ((pygame.time.get_ticks()-t) >= 1000):
        sec += 1
        t = pygame.time.get_ticks()
        #fim de jogo
        if (sec <= 60):
            if floor_collision == True:
                sec -= 1
            elif (sec >= 60):
                win = True

    #fundo preto
    display_window.fill(black)

    #colocar o texto do tempo na tela
    time_text = font.render("Time: " + str(sec) + "s", True, text_color)
    display.blit(time_text,(10,10))

    #retangulo
    rect = pygame.draw.rect(display, white, [rect_x, rect_y, 100, 100])

    clock.tick(fps)
    pygame.display.update()
    pygame.display.flip()
    time.sleep(0.015)
