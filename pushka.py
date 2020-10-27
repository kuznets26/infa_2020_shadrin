from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

score = 0


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.t_live = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.x - self.r < 0:
            self.vx *= -1
        if self.x + self.r > 800:
            self.vx *= -1
        if self.y + self.r > 600:
            self.vy *= -0.8
            self.y -= self.vy
        self.vy -= gravitation
        self.x += self.vx
        self.y -= self.vy
        self.t_live += 1
        self.set_coords()

    def hittest(self, t1):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - t1.x) ** 2 + (self.y - t1.y) ** 2 < (self.r + t1.r) ** 2:
            return True
        return False

    def draw(self):
        canv.coords(self,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r
                    )

    def deletes(self):
        canv.delete(self.id)


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = 0
        self.new_target()
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(20, 50)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

        """
        global score
        self.points = score
        self.id_points = canv.create_text(100, 30, text='Счет = ' + str(self.points), font='28')
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)
        """

    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        global score
        score += int((500 / bullet) / self.r)

    def move(self):
        if self.x - self.r < 0:
            self.vx = -self.vx
        if self.x + self.r > 800:
            self.vx = -self.vx
        if self.y + self.r > 600:
            self.vy = -self.vy
            self.y -= self.vy
        if self.y - self.r < 0:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        color = self.color
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def outbound(self):
        x = self.x = -1000
        self.vx = 0
        self.vy = 0
        y = self.y
        r = self.r
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)
"""
class Shape_target():
    def __init__(self):
        self.x = rnd(100, 700)  # x
        self.y = rnd(100, 500)  # y
        self.r = rnd(30, 50)  # radius
        self.colors = ''  # colors
        self.vx = rnd(-500, 500)  # vx - speed xlabel
        self.vy = rnd(-500, 500)  # vy - speed ylabel
        self.angles = rnd(3, 9)  # quantity of angles
        self.rotation_angle = rnd(0, round(2 * m.pi))  # rotation angle
        self.omega = rnd(0, round(5 * m.pi))  # OMEGA motherfucker do you speak it???
        
    def create_shape(self):
        self.x = rnd(100, 700)  # x
        self.y = rnd(100, 500)  # y
        self.r = rnd(30, 50)  # radius
        self.colors = ''  # colors
        self.vx = rnd(-500, 500)  # vx - speed xlabel
        self.vy = rnd(-500, 500)  # vy - speed ylabel
        self.angles = rnd(3, 9)  # quantity of angles
        self.rotation_angle = rnd(0, round(2 * m.pi))  # rotation angle
        self.omega = rnd(0, round(5 * m.pi))  # OMEGA motherfucker do you speak it????

    # draws this shape
    def draw_shape(self):
        # defines vertices of the polygon
        shape_vertices = [0] * self.angles
        # counting an angle between two vertices
        alpha = 2 * m.pi / self.angles
        # creating a list of vertices
        for i in range(self.angles):
            shape_vertices[i] = (
            round(self.x + self.r * math.cos(self.rotation_angle + alpha * i)),
            round(s + Shape_Parameters[self][2] * math.sin(self.rotation_angle + alpha * i)))
        polygon(screen, Shape_Parameters[self][3], shape_vertices)

    # makes the world fly (moving and rotating the shape)
    def move_shape(n):
        global Shape_Parameters
        Shape_Parameters[n][0] += Shape_Parameters[n][4] / FPS
        Shape_Parameters[n][1] += Shape_Parameters[n][5] / FPS
        # implementing rotation
        Shape_Parameters[n][7] += Shape_Parameters[n][8] / FPS
        if Shape_Parameters[n][0] - Shape_Parameters[n][2] < 0:
            Shape_Parameters[n][4] = - Shape_Parameters[n][4]
        if Shape_Parameters[n][1] - Shape_Parameters[n][2] < 0:
            Shape_Parameters[n][5] = - Shape_Parameters[n][5]
        if Shape_Parameters[n][0] + Shape_Parameters[n][2] > width_screen:
            Shape_Parameters[n][4] = - Shape_Parameters[n][4]
        if Shape_Parameters[n][1] + Shape_Parameters[n][2] > height_screen:
            Shape_Parameters[n][5] = - Shape_Parameters[n][5]

    # checking if we hit the shape
    def shape_handle_event_hit(event, i):
        global hit
        global Shape_Parameters
        # counting an angle between two vertices
        alpha = 2 * m.pi / Shape_Parameters[i][6]
        f = True
        for j in range(Shape_Parameters[i][6]):
            # counting vector between 2 neighbouring vertices
            a_x = Shape_Parameters[i][0] + Shape_Parameters[i][2] * m.cos(Shape_Parameters[i][7] + alpha * j)
            a_y = Shape_Parameters[i][1] + Shape_Parameters[i][2] * m.sin(Shape_Parameters[i][7] + alpha * j)
            b_x = Shape_Parameters[i][0] + Shape_Parameters[i][2] * m.cos(Shape_Parameters[i][7] + alpha * (j + 1))
            b_y = Shape_Parameters[i][1] + Shape_Parameters[i][2] * m.sin(Shape_Parameters[i][7] + alpha * (j + 1))
            # counting vector between the first neighbouring vertex and click position
            ev_point_x = event.pos[0] - a_x
            ev_point_y = event.pos[1] - a_y
            v_x = b_x - a_x
            v_y = b_y - a_y
            # counting the determinant(oriented area)
            det = - ev_point_x * v_y + ev_point_y * v_x
            if det < 0:
                f = False
                break
        if f:
            hit += 5
            create_inscription()
            create_shape(i)
            return True
        return False
"""

t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
screen2 = canv.create_text(20, 20, text=score, font='28')
g1 = gun()
bullet = 0
balls = []
targets = [t1, t2]
k = 0


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, gravitation, targets, t2, k
    canv.itemconfig(screen1, text='')
    bullet = 0
    balls = []
    gravitation = 2
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.03
    k = len(targets)
    for t in targets:
        t.new_target()
        t.live = 1
    print(k)
    while k > 0:
        for b in balls:
            b.move()
            canv.itemconfig(screen2, text=score)
            for t in targets:
                if b.hittest(t) == True:
                    t.live = 0
                    b.deletes()
                    t.outbound()
                    t.hit()
                    k -= 1
            if k <= 0:
                print('Balls')
                for b in balls:
                    b.deletes()
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canv.update()
                time.sleep(1.5)
                canv.itemconfig(screen1, text='Новая игра через 3...')
                canv.update()
                time.sleep(1)
                canv.itemconfig(screen1, text='Новая игра через 2...')
                canv.update()
                time.sleep(1)
                canv.itemconfig(screen1, text='Новая игра через 1...')
                canv.update()
                time.sleep(1)
                canv.itemconfig(screen1, text='Поехали!')
                canv.update()
                time.sleep(0.5)
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1', '')
                root.after(1000, new_game)
        for t in targets:
            t.move()
            t.draw()
        for b in balls:
            b.draw()
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.delete(gun)


new_game()

tk.mainloop()
