from turtle import Turtle
from random import random
def random_color():
    return(random(),random(),random())
#lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel
senora_sad_burritto = Turtle()
senora_sad_burritto.pensize(random())
senora_sad_burritto.pencolor(random_color())

jason = Turtle()
jason.pensize(5)
jason.pencolor('cyan')
#lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel
def saovar():
    acolor=input('Asuna pen color?')
    asize=input('Asuna pensize?')
    asuna = Turtle()
    asuna.pensize(asize)
    asuna.pencolor(acolor)

    kicolor=input('Kirito pen color?')
    kisize=input('Kirito pensize?')
    kirito = Turtle()
    kirito.pensize(kisize)
    kirito.pencolor(kicolor)

    klcolor=input('Klein pen color?')
    klsize=input('Klein pensize?')
    klein = Turtle()
    klein.pensize(klsize)
    klein.pencolor(klcolor)
#lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel
def saoturtle():
    for count in range(6):
        asuna.forward(107)
        asuna.right(60)
    for count in range(9):
        klein.forward(99)
        klein.left(40)
    kirito.forward(72)
    while True:
        kirito.forward(20)
        kirito.right(5)
#lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel
def spirograph():
    while True:
        for count in range(4):
            jason.pencolor(random_color())
            jason.forward(100)
            jason.right(90)
        jason.left(5)
#lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel lel
def sadburritto():
    for count in range(3):
        senora_sad_burritto.forward(250)
        senora_sad_burritto.right(120)
