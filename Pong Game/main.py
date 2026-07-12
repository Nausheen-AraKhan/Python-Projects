from turtle import Screen
from pong_paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard
screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)
r_paddle=Paddle(370,0)
l_paddle=Paddle(-370,0)
ball=Ball()
score=ScoreBoard()
ball.speed(0.1)
screen.tracer(1,0)
is_game_on=False
screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="a")
screen.onkey(fun=l_paddle.go_down,key="z")
is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50  and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_pos()
        score.l_point()
    if ball.xcor()<-380:
        ball.reset_pos()
        score.r_point()
screen.exitonclick()
