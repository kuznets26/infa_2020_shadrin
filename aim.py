import pygame
from math import sqrt
from pygame.draw import *
from random import randint
pygame.init()
FPS = 60
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()
#Цвета
if 0==0:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE=(255,255,255)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
#Новый шарик
def new_ball():
    global x, y, r
    x = randint(200,800)
    y = randint(100,500)
    r = randint(25,60)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
#Статистика
def score():
    global popal,promazal
    polygon(screen, (132, 229, 5), [(0, 0), (240, 0),
                                    (240, 140), (0, 140)])
    inscription_font = pygame.font.SysFont('Arial Black', 20)
    inscription = inscription_font.render("Попал = "+ str(popal), 5, WHITE)
    inscription1 = inscription_font.render("Промазал = "+ str(promazal), 5, (WHITE))
    if popal+promazal>0:
        inscription2 = inscription_font.render("Успешность = " + str(int(popal*100/(promazal+popal)))+"%", 5, WHITE)
    else:
        inscription2 = inscription_font.render("Успешность = " + str(100) + "%", 5, WHITE)
    screen.blit(inscription, (10, 0))
    screen.blit(inscription1, (10, 50))
    screen.blit(inscription2, (10, 100))

pygame.display.update()
finished = False
promazal=0
popal=0
new_ball()
score()
pygame.display.update()
start_time = pygame.time.get_ticks()
while not finished:
    clock.tick(FPS)
    if (pygame.time.get_ticks() - start_time > 700 + (60 - r) * 10):#Проверка на слоупока
        promazal += 1
        screen.fill(BLACK)
        score()
        new_ball()
        start_time = pygame.time.get_ticks()
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ((event.pos[0]-x)**2+(event.pos[1]-y)**2)<r**2:#Проверка на попадание
                screen.fill(BLACK)
                popal += 1
                score()
                new_ball()
                start_time=pygame.time.get_ticks()
                pygame.display.update()
            else:
                promazal+=1
                score()
                pygame.display.update()


pygame.quit()