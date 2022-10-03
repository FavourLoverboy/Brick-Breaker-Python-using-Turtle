from turtle import Turtle
STARTING_POSITION = (0, -280)
PLAYER_MOVEMENT = 60

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.shape('square')
        self.shapesize(stretch_len=12, stretch_wid=1)

    def move_right(self):
        if not self.xcor() > 500:
            self.forward(PLAYER_MOVEMENT)

    def move_left(self):
        if not self.xcor() < -500:
            self.backward(PLAYER_MOVEMENT)
