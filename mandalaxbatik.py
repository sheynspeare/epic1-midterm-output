#Shayne B. Yanson BSCS 1B
import turtle
from math import pi

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('#0c0c0c')
t.color('white')

#sun
while True:
    t.speed(20)
    t.pensize(1)
    t.fd(100)
    t.lt(-80)
    t.rt(30)
    if abs(t.pos()) < 1:
        break

#disk
t.penup()
t.goto(50, -57)
t.pendown()
t.pensize(16)
t.speed(5)

r=22
t.circle(r)

#pentagon
t.penup()
t.goto(50, -34)
t.pendown()
t.pensize(1.35)
t.speed(17)
t.color('yellow')

for i in range (8):
    for j in range (5):
        t.rt(72)
        t.fd(100)
    t.rt(45)

#thinnest circle
t.penup()
t.goto(50, -105)
t.pendown()
t.speed(8)
t.color('white')

r=70
t.circle(r)

#dotted circle
DOT_DIAMETER = 5
def draw_circle(radius):
    turtle.color('white')
    turtle.penup()
    turtle.speed(60)
    turtle.goto(50, -115)

    circumference = 2 * pi * radius

    dot_extent = 360 * DOT_DIAMETER*2 / circumference  # diameter to angle

    extent = 0
    while extent < 360:
        turtle.dot(DOT_DIAMETER)
        turtle.circle(radius, extent=dot_extent)

        extent += dot_extent

draw_circle(78)

#thicc circle
t.penup()
t.goto(50, -128)
t.pendown()
t.pensize(7)
t.speed(10)

r=93
t.circle(r)

#thin circle
t.penup()
t.goto(50, -141)
t.pendown()
t.pensize(2)
t.speed(10)

r=105
t.circle(r)

#thickest circle
t.penup()
t.goto(50, -160)
t.pendown()
t.pensize(23)
t.speed(10)

r=125
t.circle(r)

#outer circle
t.penup()
t.goto(50, -200)
t.pendown()
t.pensize(9)
t.speed(10)

r=165
t.circle(r)

turtle.exitonclick()

