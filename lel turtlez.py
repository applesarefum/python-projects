from turtle import Turtle
from random import random
def random_color():
    return(random(),random(),random())
albuquerque = Turtle()
albuquerque.pensize(1)
lel=1

while True:
     for count in range(4):
        albuquerque.pencolor(random_color())
        albuquerque.forward(lel)
        albuquerque.right(90)    
     albuquerque.right(10)
     lel=lel+1
