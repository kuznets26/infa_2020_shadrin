import pygame
from pygame.locals import *
from pygame.draw import *
from random import randint
import os
import matplotlib
import matplotlib.pyplot

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab

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

# drawing a graphic
fig = pylab.figure(figsize=[6, 4],  # Inches
                   dpi=200)  # 100 dots per inch, so the resulting buffer is 400x400 pixels
graf = fig.gca()
B = [100] * 20
A = [0] * 20
matplotlib.pyplot.xlabel(r'Время')
matplotlib.pyplot.ylabel(r"Успешность")
graf.plot(A)
canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
FPS = 200
screen = pygame.display.set_mode((1200, 800))

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0, 0))
clock = pygame.time.Clock()
X1, Y1, X2, Y2 = 0, 0, 1200, 800


# creating an inscription after 2 seconds of 100% hits
def KRASAWWWA():
    inscription_font = pygame.font.SysFont('Arial Black', 60)
    inscription = inscription_font.render("KRASAWWWA, 100% POPADANIE", 5,
                                          (randint(1, 254), randint(1, 254), randint(1, 254)))
    screen.blit(inscription, (100, 0))


# drawing background
def draw_background():
    screen.blit(surf, (0, 0))
    polygon(screen, GREEN, [(X1, Y1), (X1, Y2), (X2, Y2), (X2, Y1)], 5)
    if (success == 100) and (hit > 0):
        KRASAWWWA()


# drawing new ball
def new_ball(n):
    ball_params[n][0] = randint(((2 * X1 + X2) // 3), round(X2 // 1.5))  # x
    ball_params[n][1] = randint(round((2 * Y1 + Y2) // 3), round(Y2 // 1.5))  # y
    ball_params[n][2] = randint(25, 50)  # r
    ball_params[n][3] = COLORS[randint(0, 5)]  # colors
    ball_params[n][4] = randint(-500, 500) + 1  # vx
    ball_params[n][5] = randint(-500, 500) + 1  # vy
    ball_params[n][6] = pygame.time.get_ticks()


# drawing score
def score():
    global hit, miss
    inscription_font = pygame.font.SysFont('Arial Black', 20)
    inscription = inscription_font.render("Попал = " + str(hit), 5, BLACK)
    inscription1 = inscription_font.render("Промазал = " + str(miss), 5, BLACK)
    if hit + miss > 0:
        inscription2 = inscription_font.render("Успешность = " + str(int(hit * 100 / (miss + hit))) + "%", 5,
                                               BLACK)
    else:
        inscription2 = inscription_font.render("Успешность = " + str(100) + "%", 5, BLACK)
    screen.blit(inscription, (10, 0))
    screen.blit(inscription1, (10, 25))
    screen.blit(inscription2, (10, 50))


# checking if we hit the ball
def check(n, x, y):
    global ball_params
    if (((x - ball_params[n][0]) ** 2 + (y - ball_params[n][1]) ** 2) < ball_params[n][2] ** 2):
        return True
    else:
        return False


# checking if we hit the ball and creates a new ball
def handler(n):
    global hit
    global s
    global start_time
    if check(n, event.pos[0], event.pos[1]):
        hit += 1
        s = 1
        new_ball(n)
        start_time = pygame.time.get_ticks()


# drawing a ball
def draw_ball(n):
    global screen
    global ball_params
    circle(screen, ball_params[n][3], (ball_params[n][0], ball_params[n][1]), ball_params[n][2])


# checking if we need to blow the destruction up
def destruction(n):
    global miss
    if ball_params[n][2] > 90:  # Такой порядок для того, чтобы не улетали за границ, Уничтожение
        miss += 1
        new_ball(n)
    elif pygame.time.get_ticks() - ball_params[n][6] > 60:  # Увеличение
        ball_params[n][2] += 1
        ball_params[n][6] = pygame.time.get_ticks()


# moving the ball
def move_ball(n):
    global miss
    if ball_params[n][0] - ball_params[n][2] < X1:
        ball_params[n][4] *= -1
        ball_params[n][0] += 3 * ball_params[n][4] // FPS
    if ball_params[n][0] + ball_params[n][2] > X2:  # Проверка стены
        ball_params[n][4] *= -1
        ball_params[n][0] += 3 * ball_params[n][4] // FPS
    if ball_params[n][1] - ball_params[n][2] < Y1:
        ball_params[n][5] *= -1
        ball_params[n][1] += 3 * ball_params[n][5] // FPS
    if ball_params[n][1] + ball_params[n][2] > Y2:
        ball_params[n][5] *= -1
        ball_params[n][1] += 3 * ball_params[n][5] // FPS
    ball_params[n][0] += ball_params[n][4] // FPS  # Передижение
    ball_params[n][1] += ball_params[n][5] // FPS


# for graph(unknown function)
def sdvig(c):
    for i in range(19):
        A[i] = A[i + 1]
    A[19] = c


# building a graphic
def graphic():
    global time0, success, miss_prev, hit_prev, hit, miss, B, fig, graf, canvas, renderer, raw_data, surf
    if pygame.time.get_ticks() - time0 > 2000:
        time0 = pygame.time.get_ticks()
        if (hit + miss - hit_prev - miss_prev) == 0:
            success = 0
        else:
            success = 100 * (hit - hit_prev) / (hit + miss - hit_prev - miss_prev)
        sdvig(success)
        miss_prev = miss
        hit_prev = hit
        B = [(hit * 100) / (hit + miss)] * 20

        fig = pylab.figure(figsize=[6, 4],  # Inches
                           dpi=200)  # 100 dots per inch, so the resulting buffer is 400x400 pixels
        matplotlib.pyplot.xlabel(r'Время')
        matplotlib.pyplot.ylabel(r"Успешность")
        graf = fig.gca()
        graf.plot(B, color='g')
        graf.plot(A, color='b')
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        surf = pygame.image.fromstring(raw_data, size, "RGB")


# starting painting
N = 8
ball_params = [0] * 15
for i in range(N):
    ball_params[i] = [0] * 7
miss = 0
miss_prev = 0
hit = 1
hit_prev = 0
s = 0
time0 = 0
success = 0
time0 = pygame.time.get_ticks()
start_time = pygame.time.get_ticks()
finished = False
for i in range(N):
    new_ball(i)
while not finished:
    clock.tick(FPS)
    graphic()
    draw_background()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(N):
                handler(i)
            if s == 0:
                miss += 1
            s = 0
    score()
    for i in range(N):
        destruction(i)
        move_ball(i)
        draw_ball(i)
    pygame.display.update()
pygame.quit()
