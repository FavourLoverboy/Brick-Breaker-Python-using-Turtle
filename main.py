import time
from turtle import Screen, screensize
from paddle import Paddle
from ball import Ball
from brick import Brick


screen = Screen()
screen.setup(width=1370, height=768)
screen.title("Coding Ninjas Brick Breaker")
screen.bgcolor("black")
screen.tracer(0)

player = Paddle()
ball = Ball()
brick = Brick()

screen.listen()
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")

# Creating The Bricks
for i in range(30):
    brick.create_brick()      

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # Detect Collistion With the Top Wall
    if ball.ycor() > 350:
        # need to bounce
        ball.bounce_y()

    # Detect Collistion With the Side Walls(Right and Left)
    if ball.xcor() > 650 or ball.xcor() < -650:
        # need to bounce
        ball.bounce_x()

    # Detect Collistion With the Paddle
    if ball.distance(player) < 150 and ball.ycor() < -245:
        # need to bounce
        ball.bounce_y()

    # Collition With Bricks
    for b in brick.bricks:
        if b.distance(ball) < 35:
            # ball.bounce_x()
            c = brick.bricks.index(b)
            brick.hid(c)


screen.mainloop()
