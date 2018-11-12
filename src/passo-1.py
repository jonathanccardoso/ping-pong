#Criar tela, bola, retângulo e tempo de jogo.

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
    game_init.fill(black)

    time_text = font.render("Time: " + str(sec) + "s", True, text_color)
    display.blit(text2,(10,10))
