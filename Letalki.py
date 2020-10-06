import pygame
from math import sqrt
from pygame.draw import *
from random import randint
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
FPS = 120
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
X1, Y1, X2, Y2 = 150, 140, 1100, 700


def chiska():
    screen.fill(BLACK)
    polygon(screen, GREEN, [(X1, Y1), (X1, Y2), (X2, Y2), (X2, Y1)], 3)
    score()


# Цвета
if 0 == 0:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# Новый шарик
def new_ball(n):
    circs[n][0] = randint(X1 + 150, X2 - 150)  # x
    circs[n][1] = randint(Y1 + 100, Y2 - 100)  # y
    circs[n][2] = randint(25, 50)  # r
    circs[n][3] = COLORS[randint(0, 5)]  # col
    a = randint(0, 1) * 2 - 1
    circs[n][4] = randint(1, 2) * a  # Vx
    a = randint(0, 1) * 2 - 1
    circs[n][5] = randint(1, 2) * a  # Vy
    circs[n][6] = pygame.time.get_ticks()
    circle(screen, circs[n][3], (circs[n][0], circs[n][1]), circs[n][2])


# Статистика
def score():
    global popal, promazal
    polygon(screen, (132, 229, 5), [(0, 0), (240, 0),
                                    (240, 140), (0, 140)])
    inscription_font = pygame.font.SysFont('Arial Black', 20)
    inscription = inscription_font.render("Попал = " + str(popal), 5, BLACK)
    inscription1 = inscription_font.render("Промазал = " + str(promazal), 5, (BLACK))
    if popal + promazal > 0:
        inscription2 = inscription_font.render("Успешность = " + str(int(popal * 100 / (promazal + popal))) + "%", 5,
                                               WHITE)
    else:
        inscription2 = inscription_font.render("Успешность = " + str(100) + "%", 5, BLACK)
    screen.blit(inscription, (10, 0))
    screen.blit(inscription1, (10, 50))
    screen.blit(inscription2, (10, 100))


def check(n, x, y):
    if (((x - circs[n][0]) ** 2 + (y - circs[n][1]) ** 2) < circs[n][2] ** 2):
        return True
    else:
        return False


N = 8
circs = [0] * 15
for i in range(N):
    circs[i] = [0] * 7
# Заполнение массива шариков
for i in range(N):
    new_ball(i)
pygame.display.update()
finished = False
promazal = 0
popal = 0
s = 0
score()
pygame.display.update()
start_time = pygame.time.get_ticks()
while not finished:
    clock.tick(FPS)
    chiska()
    for n in range(N):
        if (circs[n][0] - circs[n][2] < X1) or (circs[n][0] + circs[n][2] > X2):
            circs[n][4] *= -1
            circs[n][0] += circs[n][4]
        elif (circs[n][1] - circs[n][2] < Y1) or (circs[n][1] + circs[n][2] > Y2):
            circs[n][5] *= -1
            circs[n][1] += circs[n][5]
        elif circs[n][2] > 90:  # Такой порядок для того, чтобы не улетали за границ
            promazal += 1
            new_ball(n)
        elif (pygame.time.get_ticks() - circs[n][6]) > 60:
            circs[n][2] += 1
            circs[n][6] = pygame.time.get_ticks()
        circs[n][0] += circs[n][4]
        circs[n][1] += circs[n][5]
        circle(screen, circs[n][3], (circs[n][0], circs[n][1]), circs[n][2])

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(N):
                if check(i, event.pos[0], event.pos[1]):  # Проверка на попадание
                    chiska()
                    popal += 1
                    s = 1
                    new_ball(i)
                    start_time = pygame.time.get_ticks()
                    pygame.display.update()
            if s == 0:
                promazal += 1
                score()
                pygame.display.update()
            s = 0

pygame.quit()
