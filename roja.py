import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow = (255, 247, 0)
black = (0,0,0)
red =(255,0,0)
white = (255,255,255)

rect(screen,white,(0,0,400,400))
circle(screen,yellow, (200,200), 150)
circle(screen,red, (150,160), 30)
circle(screen,red, (250,160), 25)
circle(screen,black, (150,167), 15)
circle(screen,black, (250,167), 10)
polygon(screen,black,([120,100],[180,140],[167,153],[113,107]))
polygon(screen,black,([280,100],[220,140],[233,150],[290,110]))
polygon(screen,black,([170,300],[230,300],[230,310],[170,310]))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()