import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30

yellow = (255, 247, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
nebo = (45, 235, 235)
zemlya = (26, 166, 13)
platye_col = (232, 30, 225)
pocan_col = (129, 143, 148)
morojenka_col=(252, 228, 13)
chocolad= (210, 105, 30)


def roja(x1, x2, r):
    circle(screen, yellow, (x1, x2), r)
    circle(screen, black, (x1, x2), r, 2)
    circle(screen, red, [x1 - r // 3, x2 - r * 4 // 15], r // 5)
    circle(screen, red, (x1 + r // 3, x2 - r * 4 // 15), r // 6)
    circle(screen, black, (x1 - r // 3, x2 - r * 11 // 50), r // 10)
    circle(screen, black, (x1 + r // 3, x2 - r * 11 // 50), r // 15)
    line(screen, black, (x1, x2 - r), (x1, x2 - 1.28 * r))
    line(screen, black, (x1 - 0.71 * r, x2 - 0.71 * r), (x1 - 1.15 * r, x2 - 1.15 * r))
    line(screen, black, (x1 + 0.71 * r, x2 - 0.71 * r), (x1 + 1.15 * r, x2 - 1.15 * r))
    polygon(screen, black, (
    [x1 - r * 8 // 15, x2 - r * 2 // 3], [x1 - r * 2 // 15, x2 - r * 2 // 5], [x1 - r * 11 // 50, x2 - r * 1 // 3],
    [x1 - r * 8 // 15, x2 - r * 8 // 15]))
    polygon(screen, black, (
    [x1 + r * 8 // 15, x2 - r * 2 // 3], [x1 + r * 2 // 15, x2 - r * 6 // 15], [x1 + r * 37 // 150, x2 - r // 3],
    [x1 + r * 3 // 5, x2 - r * 3 // 5]))
    polygon(screen, black, (
    [x1 - r // 5, x2 + r * 2 // 3], [x1 + r // 5, x2 + r * 2 // 3], [x1 + r // 5, x2 + r * 11 // 15],
    [x1 - r // 5, x2 + r * 11 // 15]))
    return ()


Ecrx = 1200
Ecry = 700
screen = pygame.display.set_mode((Ecrx, Ecry))
screen.fill((250, 200, 100))
#polygon(screen, nebo, [(0, 0), (Ecrx, 0), (Ecrx, Ecry // 2), (0, Ecry // 2)])
polygon(screen, zemlya, [(0, Ecry // 2), (Ecrx, Ecry // 2), (Ecrx, Ecry), (0, Ecry)])

#Пейзаж предоставлен Косых Алексеем Б02-013
def gornychrebet1():
    x = 0.0
    y = 400.0
    Gor = [[0, 0]] * 1200
    for x in range(0, 1200):
        Gor[x] = [round(x), round(y)]
        if x < 161:
            y = 350 - 100 * (x / 100) * (x / 100)
        if (x > 160) and (x < 201):
            y = y + 1
        if (x > 200) and (x < 211):
            y = y + 5
        if (x > 210) and (x < 401):
            y = y + (375 - y) / 200
        if (x > 400) and (x < 501):
            y = y - 0.5
        if (x > 500) and (x < 541):
            y = y + 0.75
        if (x > 540) and (x < 601):
            y = y - 1 / 3
        if (x > 600) and (x < 801):
            y = y - 2 * (x - 633.3333) / 300
        if (x > 800) and (x < 1001):
            y = y + 2 * (x - 870) / 125
        if (x > 1000) and (x < 1100):
            y = y + (x - 1151) / 100
        if (x > 1100) and (x < 1197):
            y = y + (x - 1200) / 200
        if x > 1197:
            y = y + 253

    polygon(screen, [139, 109, 92], Gor)


def solntse(x, y, r):
    pygame.draw.circle(screen, [255, 255, 200], [x, y], r)
    for i in range(1, 200):
        corona = pygame.Surface((1000, 500), pygame.SRCALPHA)
        pygame.draw.circle(corona, (255, 0, 0, 0), (2 * r, 2 * r), 2 * r)
        pygame.draw.circle(corona, [255, 255, 0, 200 - i], [x, y], r + 2 * i, 2)
        screen.blit(corona, (0, 0))


def more(x, y, t):
    volna = [[0, 0]] * 100
    polygon(screen,[240,219,125],((x-15,y),(x+1000,y),(x+1000,y+250),(x-15,y+250)))
    for i in range(0, 80):
        for j in range(0, 100):
            volna[j] = [x + 10 * j, y + i * 3 + 3 * (j % 3)]
        pygame.draw.lines(screen,
                          [120 * (i + t) % 3, 120 + 30 * ((t + i) % 3) * ((i + t) % 3), 170 + 5 * ((i + t) % 3)],
                          0, volna, 3)
#Семья предоставлена Шадриным Константином Б02-001
def sharik(x, y, r):
    line(screen, black, (x, y), (x, y - r), 2)
    polygon(screen, red, ((x, y - r), (x - r / 4, y - 1.5 * r), (x + r / 4, y - 1.5 * r)))
    circle(screen,red,(round(x-0.14*r),round(y - 1.58*r)),r//6)
    circle(screen, red, (round(x + 0.14 * r), round(y - 1.58 * r)), r // 6)

def morojenka(x,y,r):
    polygon(screen,morojenka_col,((x,y),(x,y-1.1*r),(x-r*0.9,y-r*0.6)))
    circle(screen,chocolad,(round(x-r*0.7),round(y-r*0.8)),round(r*0.3))
    circle(screen, red, (round(x - r * 0.3), round(y - r * 1.1)), round(r * 0.3))
    circle(screen, white, (round(x - r * 0.65), round(y - r * 1.25)), round(r * 0.3))

def pocan(x, y, r):  # (x,y)-center ellipsa,visota
    # ruki
    line(screen, black, (x, y - r), (x - r * 4 // 5, y + r // 5), 2)
    line(screen, black, (x, y - r), (x + r * 4 // 5, y + r // 5), 2)
    morojenka(x - r * 0.75, y + r // 5,r//2)
    # nogi
    line(screen, black, (x, y + r * 3 // 5), (x - r * 0.55, y + r * 1.8), 2)
    line(screen, black, (x - r * 0.55, y + r * 1.8), (x - r * 4 // 5, y + r * 1.8), 2)
    line(screen, black, (x, y + r * 3 // 5), (x + r * 0.35, y + r * 1.8), 2)
    line(screen, black, (x + r * 0.35, y + r * 1.8), (x + r * 0.55, y + r * 1.8), 2)
    ellipse(screen, pocan_col, (x - r * 2 // 5, y - r, r * 4 // 5, 2 * r))
    ellipse(screen, black, (x - r * 2 // 5, y - r, r * 4 // 5, 2 * r), 3)
    roja(x, y - r * 9 // 10, r // 3)

def pocanessa(x, y, r):
    # ruki
    line(screen, black, (x, y - r * 0.6), (x - r * 4 // 5, y + r // 5), 2)
    line(screen, black, (x, y - r * 0.6), (x + r * 2 // 5, y - r // 5), 2)
    line(screen, black, (x + r * 2 // 5, y - r // 5), (x + r, y - r // 2), 2)
    sharik(x + r, y - r // 2, r)
    # nogi
    line(screen, black, (x, y + r * 3 // 5), (x - r * 0.55, y + r * 1.8), 2)
    line(screen, black, (x - r * 0.55, y + r * 1.8), (x - r * 4 // 5, y + r * 1.8), 2)
    line(screen, black, (x, y + r * 3 // 5), (x + r * 0.35, y + r * 1.8), 2)
    line(screen, black, (x + r * 0.35, y + r * 1.8), (x + r * 0.55, y + r * 1.8), 2)
    polygon(screen, platye_col, ((x - r * 0.55, y + r), (x, y - r), (x + r * 0.55, y + r)))
    polygon(screen, black, ((x - r * 0.55, y + r), (x, y - r), (x + r * 0.55, y + r)), 3)
    roja(x, y - r * 9 // 10, r // 3)

def semya(x,y,r):
    pocan(x-r*4//5, y, r)
    pocanessa(x+r*4//5, y, r)


gornychrebet1()

solntse(400, 100, 30)

semya(300,400,150)
semya(900,400,150)

clock = pygame.time.Clock()
finished = False
pygame.display.update()
time=0
while not finished:
    clock.tick(FPS)
    more(50, 400, round(time))
    time -=0.1
    semya(300, 400, 150)
    semya(900, 400, 150)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()