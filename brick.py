from turtle import Turtle
from random import randint

class Brick(Turtle):

    def __init__(self):
        self.bricks = []

    def create_brick(self):
        new_brick = Turtle("square")
        new_brick.shapesize(stretch_len=3, stretch_wid=1)
        new_brick.penup()
        new_brick.color("white")
        random_x = randint(-630, 630)
        random_y = randint(150, 340)
        new_brick.goto(random_x, random_y)
        self.bricks.append(new_brick)

    def hid(self, num):
        self.bricks[num].hideturtle()
