from random import randrange as rnd, choice
from random import randint
import random
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

score = 0


# Хранит информацию о шарике
class ball():
    def __init__(self, x=40, y=450, m=6600):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.rho = 14
        self.x = x
        self.y = y
        self.r = math.sqrt(m / (self.rho * math.pi))
        self.m = m
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
        self.i = ball.add_ball(self)

    def add_ball(b):
        global balls
        balls += [b]
        return len(balls) - 1

    def remove_ball(i):
        global balls
        balls[i] = 0

    # Задает координаты шарика
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

    # Рисует мячик
    def draw(self):
        canv.coords(self,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r
                    )

    # Удаляет мячик как объект
    def deletes(self):
        canv.delete(self.id)
        ball.remove_ball(self.i)


class cool_ball(ball):
    def __init__(self, x=40, y=450, m=6600):
        self.explode_time = random.random()
        self.creation_time = time.time()
        ball.__init__(self, x, y, m)

    def divide(n, negative_allowed=1):
        parts = [0] * n
        s = 0
        for i in range(n):
            k = 1 - 2 * randint(0, negative_allowed)
            parts[i] = k * random.random()
            s += parts[i]
        if abs(s) < 0.001:
            parts[0] += 1
            s += 1
        return parts, s

    def explode(self):
        global balls
        self.deletes()
        n = rnd(2, 5, 1)
        parts, s = cool_ball.divide(n, 0)
        print(parts, s)
        p_x, s_p_x = cool_ball.divide(n, 1)
        p_y, s_p_y = cool_ball.divide(n, 1)
        for i in range(n):
            m_small = parts[i] * self.m / s
            b = ball(self.x, self.y, m_small)
            b.vx = p_x[i] * self.vx * self.m / (s_p_x * m_small)
            b.vy = p_y[i] * self.vy * self.m / (s_p_y * m_small)

    def explosion_test(self):
        if time.time() - self.creation_time > self.explode_time:
            self.explode()


# Хранит информацию о пушке
class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    # Определяет начальную силу
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        l = randint(1, 3)
        if l > 1:
            new_ball = cool_ball()
        else:
            new_ball = ball()
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
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

    # Увеличение силы
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


# Создает цель для огня
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

    # Двигает цель
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

    # Рисует цель
    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        color = self.color
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    # Отводит цель на дальнее расстояние
    def outbound(self):
        x = self.x = -1000
        self.vx = 0
        self.vy = 0
        y = self.y
        r = self.r
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
screen2 = canv.create_text(20, 20, text=score, font='28')
g1 = gun()
bullet = 0
balls = []
targets = [t1, t2]
k = 0


# Основная функция игры
def new_game(event=''):
    global gun, t1, screen1, balls, bullet, gravitation, targets, t2, k, screen2
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
    while k > 0:
        for i in range(len(balls)):
            b = balls[i]
            if b != 0:
                if type(b) == cool_ball:
                    b.explosion_test()
                b.move()
                canv.itemconfig(screen2, text=score)
                for t in targets:
                    if b.hittest(t):
                        t.live = 0
                        b.deletes()
                        t.outbound()
                        t.hit()
                        k -= 1
                if k <= 0:
                    for b in balls:
                        if b != 0:
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
                    k = 0
                    root.after(1000, new_game)
        for t in targets:
            t.move()
            t.draw()
        for b in balls:
            if b != 0:
                b.draw()
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.delete(gun)


new_game()

tk.mainloop()
