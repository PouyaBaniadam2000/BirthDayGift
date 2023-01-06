from math import cos, sin, pi
import turtle

def left_age_candle_20():
    turtle.pencolor("#aa6c39")
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-50, 20)
    turtle.pendown()
    turtle.goto(-50, 60)

def right_age_candle_20():
    turtle.pencolor("#aa6c39")
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(50, 20)
    turtle.pendown()
    turtle.goto(50, 60)

def right_age_candle_20_queen():
    turtle.pencolor("#bf913b")
    turtle.penup()
    turtle.goto(30, 90)
    turtle.pendown()
    turtle.write("♕", font=("Lucida Handwriting", 40, "normal"))
    turtle.penup()

def left_age_candle_20_queen():
    turtle.pencolor("#bf913b")
    turtle.penup()
    turtle.goto(-70, 90)
    turtle.pendown()
    turtle.write("♕", font=("Lucida Handwriting", 40, "normal"))
    turtle.penup()

def left_age_candle_20_num():
    turtle.pencolor("#bf913b")
    turtle.up()
    turtle.goto(-70, 40)
    turtle.down()
    turtle.write("2", font=("Lucida Handwriting", 45, "normal"))

def right_age_candle_20_num():
    turtle.pencolor("#bf913b")
    turtle.up()
    turtle.goto(30, 40)
    turtle.down()
    turtle.write("0", font=("Lucida Handwriting", 45, "normal"))

def flames_of_candles(turtle, x, y):
    turtle.color("red")
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.write("🔥", font=("Lucida Handwriting", 20, "normal"))
    turtle.hideturtle()

def unlimited_symbol(x, y):
    turtle.pencolor("#21bede")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write("∞", font=("Lucida Handwriting", 40, "normal"))

def draw_circle(turtle, color, x, y, radius):
    turtle.speed(0.7)
    turtle.penup()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.getscreen().update()

def draw_rectangle(turtle, color, x, y, width, height):
    turtle.speed(1.3)
    turtle.hideturtle()
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)
    turtle.getscreen().update()

def draw_icing(turtle, color, y):
    turtle.speed(1.3)
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(-125, y + 10)
    turtle.pendown()
    turtle.begin_fill()

    for x in range(-125, 125):
        turtle.goto(x, y - 10 - 10 * cos((x / 100) * 2 * pi))

    turtle.goto(125, y + 10)
    turtle.goto(-125, y + 10)
    turtle.end_fill()
    turtle.getscreen().update()
