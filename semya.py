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
polygon(screen, nebo, [(0, 0), (Ecrx, 0), (Ecrx, Ecry // 2), (0, Ecry // 2)])
polygon(screen, zemlya, [(0, Ecry // 2), (Ecrx, Ecry // 2), (Ecrx, Ecry), (0, Ecry)])

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


semya(300,400,150)
semya(900,400,150)
semya(600,600,75)
semya(900,600,30)
semya(300,400,30)
semya(300,600,30)
semya(900,400,30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()