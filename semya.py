import pygame
from pygame.draw import *

pygame.init()

FPS = 60

# defining some colors
yellow = (255, 247, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
sky_color = (45, 235, 235)  # color of the sky
ground_color = (26, 166, 13)  # color of the ground
dress_color = (232, 30, 225)  # color of woman`s dress
man_color = (129, 143, 148)  # color of man`s shirt
ice_cream_color = (252, 228, 13)  # color of ice cream
chocolate_color = (210, 105, 30)  # color of chocolate

"""
FOR ALL OBJECTS FURTHER

surface = surface where the image is needed to be put
x, y = coordinates of the object(where to put object); may both be float and integer;
(x, y) = (0, 0) is in the upper right corner
r = dimension coefficient - how big is the object (float or integer)
"""


# drawing a face of a man and a woman
def face_draw(surface, x, y, r):
    # drawing head and encircling it
    circle(surface, yellow, (int(x), int(y)), int(r))
    circle(surface, black, (int(x), int(y)), int(r), 2)
    # drawing eyes
    circle(surface, red, (int(x - r // 3), int(y - r * 4 // 15)), r // 5)  # left eye
    circle(surface, red, (int(x + r // 3), int(y - r * 4 // 15)), r // 6)  # right eye
    circle(surface, black, (int(x - r // 3), int(y - r * 11 // 50)), r // 10)  # left pupil
    circle(surface, black, (int(x + r // 3), int(y - r * 11 // 50)), r // 15)  # right pupil
    # drawing hair
    line(surface, black, (int(x), int(y - r)), (int(x), int(y - 1.28 * r)))
    line(surface, black, (int(x - 0.71 * r), int(y - 0.71 * r)),
         (int(x - 1.15 * r), int(y - 1.15 * r)))
    line(surface, black, (int(x + 0.71 * r), int(y - 0.71 * r)),
         (int(x + 1.15 * r), int(y - 1.15 * r)))
    # drawing eyebrows
    polygon(surface, black, [(int(x - r * 8 // 15), int(y - r * 2 // 3)),
                             (int(x - r * 2 // 15), int(y - r * 2 // 5)),
                             (int(x - r * 11 // 50), int(y - r * 1 // 3)),
                             (int(x - r * 8 // 15), int(y - r * 8 // 15))])
    polygon(surface, black, [(int(x + r * 8 // 15), int(y - r * 2 // 3)),
                             (int(x + r * 2 // 15), int(y - r * 6 // 15)),
                             (int(x + r * 37 // 150), int(y - r // 3)),
                             (int(x + r * 3 // 5), int(y - r * 3 // 5))])
    # drawing mouth
    polygon(surface, black, [(int(x - r // 5), int(y + r * 2 // 3)),
                             (int(x + r // 5), int(y + r * 2 // 3)),
                             (int(x + r // 5), int(y + r * 11 // 15)),
                             (int(x - r // 5), int(y + r * 11 // 15))])


# defining dimensions of a screen
screen_x = 1200  # width of a display
screen_y = 700  # height of a display
# drawing a screen
screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((250, 200, 100))
# drawing a scenery
polygon(screen, ground_color, [(0, screen_y // 2), (screen_x, screen_y // 2), (screen_x, screen_y), (0, screen_y)])


# drawing sun
def sun_draw(surface, x, y, r):
    pygame.draw.circle(surface, (255, 255, 200), (x, y), r)


# drawing balloon that is being hold by woman
def balloon_draw(surface, x, y, r):
    line(surface, black, (int(x), int(y)), (int(x), int(y - r)), 2)
    polygon(surface, red, ((int(x), int(y - r)), (int(x - r / 4), int(y - 1.5 * r)),
                           (int(x + r / 4), int(y - 1.5 * r))))
    circle(surface, red, (round(x - 0.14 * r), round(y - 1.58 * r)), r // 6)
    circle(surface, red, (round(x + 0.14 * r), round(y - 1.58 * r)), r // 6)


def ice_cream_draw(surface, x, y, r):
    # drawing cone
    polygon(surface, ice_cream_color, ((int(x), int(y)), (x, int(y - 1.1 * r)),
                                       (int(x - r * 0.9), int(y - r * 0.6))))
    # drawing balls
    circle(surface, chocolate_color, (round(x - r * 0.7), round(y - r * 0.8)), round(r * 0.3))
    circle(surface, red, (round(x - r * 0.3), round(y - r * 1.1)), round(r * 0.3))
    circle(surface, white, (round(x - r * 0.65), round(y - r * 1.25)), round(r * 0.3))


# drawing arms of a man
def arms_draw_man(surface, x, y, r):
    line(surface, black, (int(x), int(y - r)), (int(x - r * 4 // 5), int(y + r // 5)), 2)  # left arm
    line(surface, black, (int(x), int(y - r)), (int(x + r * 4 // 5), int(y + r // 5)), 2)  # right arm


# drawing arms of a woman
def arms_draw_woman(surface, x, y, r):
    # drawing arms(right arm consists of 2 lines(not 1 line as in all previous variations))
    line(surface, black, (int(x), int(y - r * 0.6)), (int(x - r * 4 // 5), int(y + r // 5)), 2)  # left arm
    # first part of right arm
    line(surface, black, (int(x), int(y - r * 0.6)), (int(x + r * 2 // 5), int(y - r // 5)), 2)
    # second part of right arm
    line(surface, black, (int(x + r * 2 // 5), int(y - r // 5)), (int(x + r), int(y - r // 2)), 2)
    balloon_draw(surface, int(x + r), int(y - r // 2), int(r))
    legs_draw(surface, x, y, r)


# drawing legs
def legs_draw(surface, x, y, r):
    # drawing left leg
    line(surface, black, (int(x), int(y + r * 3 // 5)), (int(x - r * 0.55), int(y + r * 1.8)), 2)
    line(surface, black, (int(x - r * 0.55), int(y + r * 1.8)), (int(x - r * 4 // 5), int(y + r * 1.8)), 2)
    # drawing right leg
    line(surface, black, (int(x), int(y + r * 3 // 5)), (int(x + r * 0.35), int(y + r * 1.8)), 2)
    line(surface, black, (int(x + r * 0.35), int(y + r * 1.8)), (int(x + r * 0.55), int(y + r * 1.8)), 2)


# drawing a man using predefined functions
def man_draw(surface, x, y, r):
    arms_draw_man(surface, x, y, r)
    ice_cream_draw(surface, int(x - r * 0.75), int(y + r // 5), r // 2)  # man holds an ice cream
    legs_draw(surface, x, y, r)
    # drawing body and encircling it
    ellipse(surface, man_color, (int(x - r * 2 // 5), int(y - r), int(r * 4 // 5), int(2 * r)))
    ellipse(surface, black, (int(x - r * 2 // 5), int(y - r), int(r * 4 // 5), int(2 * r)), 3)
    # using predefined function to draw face
    face_draw(surface, x, y - r * 9 // 10, r // 3)


# drawing a woman using predefined functions
def woman_draw(surface, x, y, r):
    arms_draw_woman(surface, x, y, r)
    # drawing dress and encircling it
    polygon(surface, dress_color, ((int(x - r * 0.5), int(y + r)),
                                   (x, int(y - r)), (int(x + r * 0.55), int(y + r))))
    polygon(surface, black, ((int(x - r * 0.55), int(y + r)),
                             (x, int(y - r)), (int(x + r * 0.55), int(y + r))), 3)
    # using predefined function to draw face
    face_draw(surface, x, y - r * 9 // 10, r // 3)


# bringing men and women together(making a pair)
def family_draw(surface, x, y, r):
    man_draw(surface, x - r * 4 // 5, y, int(r))
    woman_draw(surface, x + r * 4 // 5, y, int(r))


sun_draw(screen, 400, 100, 1)
family_draw(screen, 300, 400, 150)
family_draw(screen, 900, 455.5, 150)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
