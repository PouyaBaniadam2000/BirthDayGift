import os
import sys
import turtle
from colorsys import hsv_to_rgb
from math import sin, cos
from pygame import mixer, init
from time import sleep

import Shapes
from Voice import *

"""
Dear Maryam

When I decided to create this program about 2 month ago ,
I really wanted to make You happy. Not just because you
were my friend , also because I loved you so much.
not just because I loved you so much , but also
because seeing you in a happy face with your gorgeous
smile , would have made me look much happier :-)
I have no idea how you are gonna react to this program and
that's killing me by the way ! :-( Anyway I just wish that you
realize how much I care for you. That's all I want right now 
and really hope it comes true. Wish to see you soon Dear Maryam :-)

From a lucky friend who loves you the most , Pouya.
                               |               |
                               |               |
                             MarMar        PoomPoom

Hope you enjoy it ❤️

3/22/2022 - 2:57 AM

Convert from base 36 to 2 ...
11011100101011111010000010110000010010100110110000010101111100101100001010101101001100111100111101011101010001010
-----------------------------------------------------------------------------------
110010001001010011010001111010111010110100011010111110110110000110000011
"""


def resource_path(relative_path):
    global base_path
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("Assets")

    return os.path.join(base_path, relative_path)


def first_slide_talks():
    turtle.bgcolor("black")
    sleep(2)
    turtle.hideturtle()
    turtle.pencolor("aqua")
    turtle.penup()
    turtle.goto(-740, 300)
    turtle.write('Dear Maryam', font=("Lucida Calligraphy", 30, "normal"))
    sleep(2)
    turtle.pencolor("Yellow")
    turtle.home()
    turtle.write("Hope You enjoy this 4 minute run 😉", move=False, align='center', font=("MV Boli", 40, "normal"))


def flower():
    hue = 0.8
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(695, 330)
    turtle.pendown()

    for _ in range(50):
        col = hsv_to_rgb(hue, 1, 1)
        hue += 0.005
        turtle.color(col, col)
        turtle.begin_fill()
        turtle.circle(50 - _, 90)
        turtle.lt(90)
        turtle.circle(50 - _, 90)
        turtle.lt(10)
        turtle.end_fill()

    hue = 0.5
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(-700, 330)
    turtle.pendown()
    _ = 0

    for _ in range(50):
        col = hsv_to_rgb(hue, 1, 1)
        hue += 0.005
        turtle.color(col, col)
        turtle.begin_fill()
        turtle.circle(50 - _, 90)
        turtle.lt(90)
        turtle.circle(50 - _, 90)
        turtle.lt(10)
        turtle.end_fill()


def colorful_main_heart():
    def love_curve(t):
        turtle.goto(0, 0)
        x = 16 * (sin(t) ** 3)
        y = 13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)
        return x, y

    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.pencolor("red")
    turtle.speed(0)

    Times_Bigger = 22

    hue = 0.3

    for i in range(0, 150):
        col = hsv_to_rgb(hue, 1, 1)
        hue += 0.05

        turtle.color(col, col)
        turtle.pencolor(col)
        x, y = love_curve(i)
        turtle.goto(x * Times_Bigger, y * Times_Bigger)
        turtle.end_fill()


"""Red Beautiful heart"""


def main_heart():
    def love_curve(t):
        turtle.goto(0, 0)
        x = 16 * (sin(t) ** 3)
        y = 13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)
        return x, y

    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.pencolor("red")
    turtle.speed(0)

    Times_Bigger = 20

    for i in range(0, 150):
        x, y = love_curve(i)
        turtle.goto(x * Times_Bigger, y * Times_Bigger)


"""Red Beautiful heart"""

"""birthday_cake"""


def birthday_cake():
    Flame_Pen = turtle.Turtle()
    Flame_Pen.hideturtle()

    Cake_Pen = turtle.Turtle()
    Cake_Pen.hideturtle()

    Candle_Pen = turtle.Turtle()
    Candle_Pen.hideturtle()

    window = turtle.Screen()
    window.bgcolor('pink')

    y = -140

    Ingredients = {}
    Ingredients["Cherry"] = "#C20067"
    Ingredients["Respberry"] = "#e30b5d"
    Ingredients["Lemon"] = "#FFFA5C"
    Ingredients["Milk Chocolate"] = "#BF671F"
    Ingredients["Dark Chocolate"] = "#2A1506"
    Ingredients["Icing"] = "#FFFFFF"
    Ingredients["Candle"] = "#F73718"

    Layers = []
    Layers.append(["Respberry", 30])
    Layers.append(["Dark Chocolate", 20])
    Layers.append(["Lemon", 60])
    Layers.append(["Milk Chocolate", 40])

    Shapes.draw_rectangle(turtle, "white", -150, y - 10, 300, 10)

    for Layer in Layers:
        Shapes.draw_rectangle(Cake_Pen, Ingredients[Layer[0]], -120, y, 240, Layer[1])
        y += Layer[1]

    Shapes.draw_icing(Cake_Pen, Ingredients["Icing"], y)
    Shapes.draw_circle(Cake_Pen, Ingredients["Cherry"], 0, y + 10, 10)

    Shapes.left_age_candle_20()
    Shapes.right_age_candle_20()

    sleep(1)

    Shapes.unlimited_symbol(-74, 5)
    Shapes.unlimited_symbol(26, 5)

    sleep(1)

    Shapes.left_age_candle_20_num()
    Shapes.right_age_candle_20_num()

    sleep(1)

    Shapes.right_age_candle_20_queen()
    Shapes.left_age_candle_20_queen()

    sleep(1)

    Shapes.flames_of_candles(Flame_Pen, -61, 146)
    Shapes.flames_of_candles(Flame_Pen, 39, 146)

    sleep(3.5)

    Wish_And_Blow()
    record_to_file("Blow_The_Candles.wav")
    Flame_Pen.clear()
    Flame_Pen.getscreen().update()
    sleep(3)
    Cake_Pen.clear()
    Cake_Pen.getscreen().update()
    turtle.clear()


"""birthday_cake"""

"""First_slide_hearts"""


def slide_hearts():
    def Curve_Side():
        for i in range(200):
            turtle.right(1)
            turtle.forward(1)

    def heart(x, y, Color):
        turtle.pensize(5)
        turtle.pencolor(Color)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(Color)
        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(113)
        Curve_Side()
        turtle.left(120)
        Curve_Side()
        turtle.forward(112)
        turtle.end_fill()

    sleep(1)

    heart(-650, -375, "blue")

    turtle.penup()
    turtle.home()

    sleep(1)

    heart(645, -375, "red")


"""First_slide_hearts"""

"""Baloons"""


def Circle_Part_Of_Baloons(x, y, radius):
    turtle.speed(0.9)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)


def left_side_of_baloons_ropes(x, y):
    turtle.hideturtle()
    turtle.pensize(4)
    i = -150
    n = 0
    c = -200
    colors = ["#22287f", "#b69521", "#ff0000", "#ad18ff", "#93e2d5", "#dc5c05"]
    for j in range(6):
        turtle.speed(10)
        turtle.pencolor("black")
        turtle.penup()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.speed(1)
        turtle.goto(i, 250)
        turtle.penup()
        turtle.pendown()
        turtle.fillcolor(colors[n])
        turtle.begin_fill()
        turtle.pencolor(colors[n])
        turtle.color()
        Circle_Part_Of_Baloons(c + 70, 205, 65)
        turtle.end_fill()
        i += -105
        n += 1
        c += -110


def right_side_of_baloons_ropes(x, y):
    turtle.speed(10)
    turtle.hideturtle()
    turtle.pensize(4)
    i = 100
    n = 0
    c = 70
    colors = ["#00ede4", "#a31e39", "#343ef7", "#fff100", "#1ac328", "#c91700"]
    for j in range(6):
        turtle.pencolor("black")
        turtle.penup()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.speed(1)
        turtle.goto(i, 250)
        turtle.penup()
        turtle.fillcolor(colors[n])
        turtle.begin_fill()
        turtle.pencolor(colors[n])
        turtle.color()
        Circle_Part_Of_Baloons(c + 30, 205, 65)
        turtle.end_fill()
        i += 110
        n += 1
        c += 110


def curve_part_of_baloons_ropes(x, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.pensize(4)
    turtle.goto(x, y)
    turtle.pendown()
    for z in range(130):
        turtle.forward(1)
        turtle.left(1)
    for t in range(75):
        turtle.right(1)
        turtle.forward(1)
    for a in range(30):
        turtle.left(1)
        turtle.forward(1)


"""Baloons"""

"""Writes I ❤️ U"""


def I_U():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-675, -400)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.write("I", font=("Lucida Handwriting", 450, "bold"))
    turtle.pendown()
    reset_turtle()
    turtle.penup()
    turtle.goto(225, -400)
    turtle.pendown()
    turtle.write("U", font=("Lucida Handwriting", 450, "bold"))


"""Writes I ❤️ U"""

"""Aftee the wish and blowing , The candles will disappear"""


def Wish_And_Blow():
    turtle.hideturtle()
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(-542, -300)
    turtle.pendown()
    turtle.write("Dear Maryam , Wish And Blow The", font=("Lucida Handwriting", 40, "normal"))
    turtle.penup()
    turtle.goto(483, -300)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.write("🕯️", font=("Lucida Handwriting", 47, "normal"))

    sleep(1)
    reset_turtle()

    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(-250, -380)
    turtle.pendown()
    turtle.write("Wish U The Bests", font=("Lucida Calligraphy", 30, "normal"))
    turtle.penup()
    turtle.goto(120, -380)
    turtle.pendown()
    turtle.pencolor("purple")
    turtle.write("😁", font=("Lucida Handwriting", 35, "normal"))


"""Aftee the wish and blowing , The candles will disappear"""

"""Go Home And Make The Direction Correct"""


def reset_turtle():
    turtle.penup()
    turtle.home()
    turtle.pendown()


"""Go Home And Make The Direction Correct"""

"""Says a Happy BirthDay to Maryam"""


def BirthDay_Text():
    turtle.pencolor("red")
    colors = ["azure", "green", "red", "yellow", "purple", "white", "aqua", "pink", "salmon", "orange", "blue",
              "yellow", "aqua"]
    turtle.bgcolor("black")
    p = 0
    for v in colors:
        turtle.pencolor(colors[p])
        turtle.hideturtle()
        turtle.write("Happy 20's BirthDay Dear Maryam 🥳", move=False, align='center',
                     font=("Lucida Handwriting", 50, "normal"))
        sleep(1)
        p += 1


"""Says a Happy BirthDay to Maryam"""

"""The Whole App"""


def Main_App():
    root = turtle.Screen()._root
    root.iconbitmap(resource_path("Image\\BirthDay.ico"))
    turtle.title("Happy BirthDay To Dear Maryam 🤩🥳")
    first_slide_talks()
    sleep(10)
    turtle.reset()
    mixer.init()
    mixer.music.load(resource_path("Audio\\SaraNaeini_JadooyeRaghsidan.ogg"))
    mixer.music.play()
    turtle.bgcolor("pink")
    curve_part_of_baloons_ropes(-502, -172)
    reset_turtle()
    left_side_of_baloons_ropes(-450, 20)
    turtle.pencolor("black")
    reset_turtle()
    curve_part_of_baloons_ropes(329, -172)
    reset_turtle()
    right_side_of_baloons_ropes(380, 20)
    reset_turtle()
    slide_hearts()
    sleep(1)
    reset_turtle()
    birthday_cake()
    turtle.reset()
    init()
    mixer.music.load(resource_path("Audio\\Birthday_Clap.ogg"))
    mixer.music.play()
    BirthDay_Text()
    sleep(1)
    turtle.reset()
    turtle.bgcolor("Black")
    sleep(0.2)
    init()
    mixer.music.load(resource_path("Audio\\ABCD_I_Love_U.ogg"))
    mixer.music.play()
    sleep(0.2)
    colorful_main_heart()
    flower()
    reset_turtle()
    turtle.penup()
    turtle.goto(-765, -385)
    turtle.pencolor("aqua")
    turtle.hideturtle()
    sleep(0.5)
    turtle.write("From POOM POOM to MAR MAR ;-)", font=("MV Boli", 28, "normal"))
    turtle.exitonclick()
    os.remove("Blow_The_Candles.wav")


"""The Whole App"""

Main_App()
