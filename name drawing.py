from turtle import Turtle
from random import random
def random_color():
    return(random(),random(),random())
letter = Turtle()
name=input('What is your name')
lettercolor=input('What color do you want your name in? (For a random color, put "random_color()"')
lettersize=input('How thick should the letters be? for a random thickness, put "random()"')
letter.pencolor(lettercolor)
letter.pensize(lettersize)
