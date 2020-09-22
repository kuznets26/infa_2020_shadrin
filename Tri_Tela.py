import math as m
from random import randint
import turtle
def kletka(x,y):
    turtle.speed(100000)
    turtle.penup()
    turtle.setpos(-x,y)
    turtle.pendown()
    turtle.shape('turtle')
    turtle.width(3)
    turtle.setheading(0)
    for i in range(2):
        turtle.forward(2*x)
        turtle.right(90)
        turtle.forward(2 * y)
        turtle.right(90)
    turtle.penup()
    turtle.setpos(0,0)
    turtle.hideturtle()

def uskorenie(nomer_chrepahi):
    PoX=(g  * massa[(nomer_cherepahi + 1) % 3] * (x[(nomer_cherepahi + 1) % 3] - x[nomer_cherepahi]) / (0.0001 + m.sqrt((x[(nomer_cherepahi + 1) % 3] - x[nomer_cherepahi]) ** 2 + (y[(nomer_cherepahi + 1) % 3] - y[nomer_cherepahi]) ** 2) ** 2.5)+
             g * massa[(nomer_cherepahi + 2) % 3] * (x[(nomer_cherepahi + 2) % 3] - x[nomer_cherepahi]) / (0.0001 + m.sqrt((x[(nomer_cherepahi + 2) % 3] - x[nomer_cherepahi]) ** 2 + (y[(nomer_cherepahi + 2) % 3] - y[nomer_cherepahi]) ** 2) ** 2.5))
    PoY=(g  * massa[(nomer_cherepahi + 1) % 3] * (y[(nomer_cherepahi + 1) % 3] - y[nomer_cherepahi]) / (0.0001 + m.sqrt((x[(nomer_cherepahi + 1) % 3] - x[nomer_cherepahi]) ** 2 + (y[(nomer_cherepahi + 1) % 3] - y[nomer_cherepahi]) ** 2) ** 2.5)+
             (g  * massa[(nomer_cherepahi + 2) % 3] * (y[(nomer_cherepahi + 2) % 3] - y[nomer_cherepahi]) / (0.0001 + m.sqrt((x[(nomer_cherepahi + 2) % 3] - x[nomer_cherepahi]) ** 2 + (y[(nomer_cherepahi + 2) % 3] - y[nomer_cherepahi]) ** 2) ** 2.5)))
    return(PoX,PoY)

def Chek():
    if abs(Vx[nomer_cherepahi])>limit :
        Vx[nomer_cherepahi]*=0.8
    if abs(Vy[nomer_cherepahi]) > limit:
        Vy[nomer_cherepahi]*=0.8
V=0
g=1100
maxm=10
limit=30


Razmerx=680
Razmery=320

kletka(Razmerx,Razmery)
Vx=[0.0]*3
Vy=[0.0]*3
x=[0.0]*3
y=[0.0]*3
Ax=[0.0]*3
Ay=[0.0]*3
massa=[0]*3

SemyaCherepah = [turtle.Turtle(shape='turtle') for i in range(3)]
nomer_cherepahi=0
for unit in SemyaCherepah:
    Vx[nomer_cherepahi]=randint(-V,V)
    Vy[nomer_cherepahi]=randint(-V,V)
    x[nomer_cherepahi] = randint(-Razmerx, Razmerx)
    y[nomer_cherepahi] = randint(-Razmery, Razmery)
    massa[nomer_cherepahi] = randint(4, maxm)
    unit.penup()
    unit.speed(100)
    unit.shapesize(0.3*massa[nomer_cherepahi])
    unit.goto(x[nomer_cherepahi],y[nomer_cherepahi])
    nomer_cherepahi+=1
nomer_cherepahi=0

for PovtoriKRaz in range(1000000000):
    nomer_cherepahi=0
    for unit in SemyaCherepah:

        x[nomer_cherepahi]+=Vx[nomer_cherepahi]#+round(Ax[nomer_cherepahi]/2)
        y[nomer_cherepahi]+=Vy[nomer_cherepahi]#+round(Ay[nomer_cherepahi]/2)
        unit.goto(x[nomer_cherepahi], y[nomer_cherepahi])
        if m.fabs(x[nomer_cherepahi]) >Razmerx-5 :
            Vx[nomer_cherepahi]=-Vx[nomer_cherepahi]
            x[nomer_cherepahi] += Vx[nomer_cherepahi]
            unit.goto(x[nomer_cherepahi], y[nomer_cherepahi])
        if m.fabs(y[nomer_cherepahi]) >Razmery-5 :
            Vy[nomer_cherepahi] = -Vy[nomer_cherepahi]
            y[nomer_cherepahi] += Vy[nomer_cherepahi]
            unit.goto(x[nomer_cherepahi], y[nomer_cherepahi])
        Vx[nomer_cherepahi]+=Ax[nomer_cherepahi]
        Vy[nomer_cherepahi]+=Ay[nomer_cherepahi]
        Chek()
        Ax[nomer_cherepahi] = (uskorenie(nomer_cherepahi)[0])
        Ay[nomer_cherepahi] = (uskorenie(nomer_cherepahi)[1])
        nomer_cherepahi+=1
