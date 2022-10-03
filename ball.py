from turtle import Turtle
from random import randint

STARTING_POSITION = (0, -245)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.goto(STARTING_POSITION)
        self.shape('circle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.09
        self.direction = randint(1, 2)

    def ball_move(self):
        if self.direction == 1:
            self.direction = 2
            self.x_move = -10
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 

    def bounce_x(self):
        self.x_move *= -1

        