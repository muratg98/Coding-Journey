import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scores import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

user1 = Paddle((350, 0))
user2 = Paddle((-350, 0))
user1_score = Score((150, 250))
user2_score = Score((-150, 250))
ball = Ball()

screen.listen()

screen.onkeypress(user1.up, "Up")
screen.onkeypress(user1.down, "Down")
screen.onkeypress(user2.up, "w")
screen.onkeypress(user2.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(user1) < 50 and ball.xcor() > 320 or ball.distance(user2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 400:
        time.sleep(0.25)
        ball.reset_position()
        time.sleep(0.25)
        ball.x_move = -10
        ball.y_move = -10
        user2_score.update_score()
    elif ball.xcor() < -400:
        time.sleep(0.25)
        ball.reset_position()
        time.sleep(0.25)
        ball.x_move = 10
        ball.y_move = 10
        user1_score.update_score()

    screen.update()

screen.exitonclick()


