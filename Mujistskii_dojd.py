import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30


yellow = (255, 247, 0)
black = (0,0,0)
red =(255,0,0)
white = (255,255,255)
nebo= (45, 235, 235)
zemlya=(26, 166, 13)
platye_col=(232, 30, 225)
pocan_col=(129, 143, 148)
morojenka_col=(229, 232, 44)
def roja(x1,x2,r):
    circle(screen,yellow, (x1,x2), r)
    circle(screen, black, (x1, x2), r,2)
    circle(screen, red, [x1 - r // 3, x2 - r * 4 // 15], r // 5)
    circle(screen,red, (x1+r//3,x2-r*4//15), r//6)
    circle(screen,black, (x1-r//3,x2-r*11//50), r//10)
    circle(screen,black, (x1+r//3,x2-r*11//50), r//15)
    polygon(screen,black,([x1-r*8//15,x2-r*2//3],[x1-r*2//15,x2-r*2//5],[x1-r*11//50,x2-r*1//3],[x1-r*8//15,x2-r*8//15]))
    polygon(screen,black,([x1+r*8//15,x2-r*2//3],[x1+r*2//15,x2-r*6//15],[x1+r*37//150,x2-r//3],[x1+r*3//5,x2-r*3//5]))
    polygon(screen,black,([x1-r//5,x2+r*2//3],[x1+r//5,x2+r*2//3],[x1+r//5,x2+r*11//15],[x1-r//5,x2+r*11//15]))
    return()

Ecrx=1200
Ecry=700
screen = pygame.display.set_mode((Ecrx, Ecry))
polygon(screen,nebo,[(0,0),(Ecrx,0),(Ecrx,Ecry//2),(0,Ecry//2)])
polygon(screen,zemlya,[(0,Ecry//2),(Ecrx,Ecry//2),(Ecrx,Ecry),(0,Ecry)])
def pocan(x,y,r) :
    line(screen, black, (x, y - r), (x - r * 4 // 5, y + r // 5), 2)
    line(screen, black, (x, y - r), (x + r * 4 // 5, y + r // 5), 2)
    line(screen, black, (x, y + r*3//5), (x - r*0.55, y + r *1.8), 2)
    line(screen, black, (x - r*0.55, y + r * 1.8),(x - r * 4 // 5, y + r * 1.8), 2)
    line(screen, black, (x, y + r * 3 // 5), (x + r * 0.35, y + r * 1.8), 2)
    line(screen, black, (x + r * 0.35, y + r * 1.8),(x + r*0.55 , y + r * 1.8), 2)
    ellipse(screen,pocan_col,(x-r*2//5,y-r,r*4//5,2*r))
    ellipse(screen, black, (x - r * 2 // 5, y - r, r * 4 // 5, 2 * r), 3)
    roja(x,y-r*9//10,r//3)


k_pocanov=700
kachalka = [0] * k_pocanov
for i in range(k_pocanov):
    kachalka[i] = [0] * 3
for i in range(k_pocanov):
    kachalka[i][ 0] = randint(0,Ecrx)
    kachalka[i][ 1] = randint(-15*Ecry,Ecry//2)
    kachalka[i][ 2] = randint(75,150)
#pocan(380,400,150)
#roja(500,500,500)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    polygon(screen, nebo, [(0, 0), (Ecrx, 0), (Ecrx, Ecry // 2), (0, Ecry // 2)])
    polygon(screen, zemlya, [(0, Ecry // 2), (Ecrx, Ecry // 2), (Ecrx, Ecry), (0, Ecry)])
    for i in range(k_pocanov):
        kachalka[i][1]+=20
        if(kachalka[i][1]+kachalka[i][2]>0):
            pocan(kachalka[i][0],kachalka[i][1],kachalka[i][2])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()