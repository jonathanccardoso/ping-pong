import pygame, sys, time, random
from pygame.locals import *

def game_init(w,h):
    pygame.init()
    #size tela
    width,height = w,h
    size = width,height
    #modo do display do pygame
    display = pygame.display.set_mode(size)
    #name project
    pygame.display.set_caption("Ping Pong")
    return display

pygame.init()

width = 640 #800
height = 480 #600

screen = pygame.display.set_mode((640, 480))
display = game_init(640,480)

#time
sec = 0
t = pygame.time.get_ticks()

fps = 25
clock = pygame.time.Clock()
font = pygame.font.Font(None,30)
text_color= (0,200,200)

black = (0, 0, 0)
white = (255, 255, 255)

# Posicao inicial do retangulo e da bola
rect_x = 272
rect_y = 470

### Music ###
music = pygame.mixer.Sound('musics/endofline.ogg')

display_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('PingPong')

game_over = False
colisao_chao = False
win = False

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

x_cor = random.randint(15, width - 15)
y_cor = random.randint(15, height - 15)

x_change = random.randint(3, 7)
y_change = random.randint(3, 7)

coordinates = []

while not game_over:

	for event in pygame.event.get():
	    if event.type == QUIT:
	        pygame.quit()
	        sys.exit()

	    if event.type == KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            pygame.quit()
	            sys.exit()

	key = pygame.key.get_pressed()

	music.play()

	#moving player
	if key[pygame.K_LEFT]:
	  rect_x -= 5
	  if rect_x < 0:
	    rect_x = 0
	if key[pygame.K_RIGHT]:
	  rect_x += 5
	  if rect_x > 532:
	    rect_x = 540
    
	#time jogando
	if ((pygame.time.get_ticks()-t) >= 1000):
	    sec += 1
	    t = pygame.time.get_ticks()
	    #fim de jogo
	    if (sec <= 60):
	      if colisao_chao == True:
	      	#stop time
	        sec-=1
	      elif sec >= 60: #and colisao_chao == False:
	    	win = True

	x_cor += x_change
	y_cor += y_change

	display_window.fill(black)

	text2=font.render("Time: "+str(sec)+"s",True,text_color)
  	display.blit(text2,(10,10))

	for coordinate in coordinates:
	    circle = pygame.draw.circle(display_window, white, (coordinate[0], coordinate[1]), 15, 0)

	circle = pygame.draw.circle(display_window, white, (x_cor, y_cor), 15, 0)

	rect = pygame.draw.rect(screen, white, [rect_x, rect_y, 100, 100])

	#logica para ganhar ou perder
	if colisao_chao == True:
	  screen.fill(black)
	  music.stop()
	  text_fim=font.render("Game Over!",True,text_color)
	  text_fim_rect = text_fim.get_rect()
	  text_fim_rect.center=(display.get_width()//2, display.get_height()//2)
	  display.blit(text_fim,text_fim_rect)
	elif win == True:
	  screen.fill(black)
	  music.stop()
	  text_fim=font.render("You Win!",True,text_color)
	  text_fim_rect = text_fim.get_rect()
	  text_fim_rect.center=(display.get_width()//2, display.get_height()//2)
	  display.blit(text_fim,text_fim_rect)

	if x_cor > (width - 15) or x_cor < 15:
	    x_change = x_change * -1
	if y_cor > (height - 15) or y_cor < 15:
	    y_change = y_change * -1
	if circle.colliderect(rect):
		y_change = y_change * -1
	if y_cor > 460:
		#colisao no chao
		colisao_chao = True
		y_change = y_change * -1

	clock.tick(fps)
	pygame.display.update()
	pygame.display.flip()
  	time.sleep(0.015)
