from turtle import *
hideturtle()
speed(0)

def move(x, y):
    penup()
    goto(x, y)
    pendown()

def draw_circle(x, y):
    move(x, y)
    begin_fill()
    circle(25)
    end_fill()

def star(x, y):
    pensize(10)
    color("yellow")
    move(x, y)
    begin_fill()
    for i in range(5):
        forward(20)
        right(144)
    end_fill()

color("#131862")
move(-500, -500)
begin_fill()
for i in range(4):
    forward(1000)
    left(90)
end_fill()

color("green")
move(-500, -100)
begin_fill()
for i in range(4):
    forward(1000)
    right(90)
end_fill()

color("black")
draw_circle(100, -100)
draw_circle(300, -100)
color("yellow")
move(50, -50)
begin_fill()
forward(300)
left(90)
forward(50)
left(90)
forward(75)
right(90)
forward(50)
left(90)
forward(150)
left(90)
forward(50)
right(90)
forward(75)
left(90)
forward(50)
end_fill()
left(90)

color("red")
move(-400, -100)
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()

color("brown")
move(-325, -100)
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)
end_fill()

color("black")
move(-450, 100)
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

star(100, 300)
star(150, 250)
star(-10, 250)
star(400, 275)
star(300, 275)

exitonclick()