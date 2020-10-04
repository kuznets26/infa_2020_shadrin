import pygame
from pygame.draw import *
from math import pi, cos, sin

pygame.init()
FPS = 60
screen1 = pygame.display.set_mode((1200, 800))
rect(screen1, (214, 214, 208), (0, 0, 1600, 900))


def generator(x, y, d_c):  # Побочная функция для рукава, возвращает массив значений вершин от центра руки
    A = [(int(x - 90 * d_c), int(y)),
         (int(x - 40 * d_c), int(y - 80 * abs(d_c))),
         (int(x + 40 * d_c), int(y - 30 * abs(d_c))),
         (int(x + 50 * d_c), int(y + 30 * abs(d_c))),
         (int(x - 30 * d_c), int(y + 80 * abs(d_c)))]
    return A


def Obvodka(screen, col, A):
    """
    Рисует обведенный полигон цвета col, по массиву точек А
    """
    polygon(screen, col, A)
    polygon(screen, (0, 0, 0), A, 1)


def ruka(screen, t_shirt_color: tuple, body_color: tuple,
         x: int, y: int, d_c: float):
    """
    Рисует Правую руку, если d_c>0, Левю руку, если d_c<0.
    :param (x,y): Центр руки
    :param d_c: Коэффицент увеличения
    """

    polygon(screen, body_color,
            [(int(x - 30 * d_c), int(y - 10 * abs(d_c))), (int(x + 100 * d_c), int(y - 440 * abs(d_c))),
             (int(x + 120 * d_c), int(y - 440 * abs(d_c))), (int(x), int(y))])
    circle(screen, body_color, (int(x + 90 * d_c), int(y - 415 * abs(d_c))), int(40 * abs(d_c)))
    circle(screen, (255, 229, 204), (int(x + 90 * d_c), int(y - 415 * abs(d_c))), int(40 * abs(d_c)), 1)
    # Рукав
    Obvodka(screen, t_shirt_color, generator(x, y, d_c))


def shevelura(screen, col, x, y, R, d, n):
    """
    Рисует волосы цвета col на экране. Ввводить параметры головы, высоту волоса, количество "волос"(Желательно >5, <30)
    :param (x,y):Центр головы
    :param R: Радиус головы
    :param d: Высота волоса
    :param n: Количество волос

    """
    for i in range(n):
        f = pi / 4 + i * pi / n / 2 + pi / n / 4
        Obvodka(screen, col, [(x + cos(f - pi / n / 3) * R, y - sin(f - pi / n / 3) * R),
                              (x + cos(f) * (R + d), y - sin(f) * (R + d)),
                              (x + cos(f + pi / n / 3) * R, y - sin(f + pi / n / 3) * R)])


def transfer(screen, t_shirt_color: tuple, body_color: tuple,
             eye_color: tuple, triangle_color: tuple,
             x: int, y: int, d_c: float):
    """
        Функция рисует Радостного мальчика с поднятыми рками
        Задаются цвета, левая верхняя точка, коэффицент увеличения.
    """
    x -= 70 * d_c
    y -= 24 * d_c
    # a boy holding a sign
    circle(screen, t_shirt_color, (int(x + 400 * d_c), int(y + 650 * d_c)), int(240 * d_c))  # body
    circle(screen, body_color, (int(x + 400 * d_c), int(y + 300 * d_c)), int(180 * d_c))  # head
    ruka(screen, t_shirt_color, body_color, x + 600 * d_c, y + 480 * d_c, d_c)  # Правая рука
    ruka(screen, t_shirt_color, body_color, x + 200 * d_c, y + 480 * d_c, -d_c)  # Левая рука
    ellipse(screen, eye_color, (int(x + 420 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)))  # right eye
    ellipse(screen, (0, 0, 0), (int(x + 420 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)), 1)
    ellipse(screen, eye_color, (int(x + 290 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)))  # left eye
    ellipse(screen, (0, 0, 0), (int(x + 290 * d_c), int(y + 220 * d_c), int(90 * d_c), int(80 * d_c)), 1)
    ellipse(screen, (0, 0, 0),
            (int(x + 453 * d_c), int(y + 255 * d_c), int(25 * d_c), int(20 * d_c)))  # right small eye
    ellipse(screen, (0, 0, 0), (int(x + 323 * d_c), int(y + 255 * d_c), int(25 * d_c), int(20 * d_c)))  # left small eye
    Obvodka(screen, (94, 50, 0), [(int(x + 400 * d_c), int(y + 342 * d_c)),#Нос
                                  (int(x + 417 * d_c), int(y + 310 * d_c)),
                                  (int(x + 383 * d_c), int(y + 310 * d_c))])
    Obvodka(screen, (212, 2, 2), [(int(x + 400 * d_c), int(y + 420 * d_c)),#Рот
                                  (int(x + 500 * d_c), int(y + 370 * d_c)),
                                  (int(x + 300 * d_c), int(y + 370 * d_c))])
    shevelura(screen1, triangle_color, x + 400 * d_c, y + 300 * d_c, int(180 * d_c), 30 * d_c, 10)  # волосы


def sign(screen, x1: int, y1: int, d_c: float):
    # Рисует плакат
    # x1 - x of a first boy   y1 - y of a first boy
    # a sign "Python`s amazing
    polygon(screen, (132, 229, 5), [(x1, int(y1 - 50 * d_c)), (int(x1 + 1400 * d_c), int(y1 - 50 * d_c)),
                                    (int(x1 + 1400 * d_c), int(y1 + 50 * d_c)), (x1, int(y1 + 50 * d_c))])  # banner
    inscription_font = pygame.font.SysFont('Arial Black', int(82 * d_c))
    inscription = inscription_font.render("PYTHON IS REALLY AMAZING", 5, (0, 0, 0))  # inscription
    screen.blit(inscription, (int(x1 + 35 * d_c), int(y1 + (-60) * d_c)))  # where to


def fanati(x1, y1, d_c):
    """
    Рисует двх мальчиков с плакатом
    :param x1,y1: Верхняя левая точка картинки
    :param d_c: Увеличение картинки
    """
    # Вычисление требемых параметров
    y1 += 53 * d_c
    x2 = x1 + int(600 * d_c)
    y2 = y1
    # Мальчик1
    transfer(screen1, tshrt_color1, color_1, eye_color1, hair_color1, x1 + 35, y1, d_c)
    # Мальчик2
    transfer(screen1, tshrt_color2, color_2, eye_color2, hair_color2, x2 + 35, y2, d_c)
    # Плакат
    sign(screen1, x1, y1, d_c)


""" 
    color_1 - color of a first boy
    color_2 - color of a second boy
    tshrt_color1 - t-shirt color of a first boy
    tshrt_color2 - t-shirt color of a second boy
    hair_color1 - hair color of a first boy
    hair_color2 - hair color of a second boy
    eye_color1 - eye color of a first boy
    eye_color2 - eye color of a second boy
"""
x1 = 0
y1 = 0
Razmer = 700
# Используемые цвета
color_1 = (252, 252, 202)
color_2 = (247, 235, 121)
tshrt_color1 = (177, 221, 252)
tshrt_color2 = (223, 227, 5)
hair_color1 = (87, 24, 4)
hair_color2 = (7, 140, 36)
eye_color1 = (67, 195, 250)
eye_color2 = (67, 240, 220)
d_c = Razmer / 1400.0  # вычисления коэффицента увеличения

fanati(x1, y1, d_c)  # Вызов функции отрисовки по параметрам
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
