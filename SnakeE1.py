import random
from distutils.core import setup
from random import randrange
from turtle import *

from freegames import square, vector

color1 = random.randint(0, 4)
color2 = random.randint(0, 4)

while color2 == color1:
    color2 = random.randint(0, 4)

color3 = ['blue', 'purple', 'pink', 'green', 'black']
color4 = ['blue', 'purple', 'pink', 'green', 'black']

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color3[color1])

    square(food.x, food.y, 9, color4[color2])
    update()
    ontimer(move, 100)


def movefood():
    food.x += randrange(-10, 11, 10)
    food.y += randrange(-10, 11, 10)
    ontimer(movefood, 500)


setup()
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()
donbe()
