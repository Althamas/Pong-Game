from paddles import *
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
Game_is_on = True
while Game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    if ball.distance(paddle1) < 45 and ball.xcor() > 320 or ball.distance(paddle2) < 45 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed() + 0.1

    elif ball.xcor() > 350:
        score.score1 += 1
        score.increase_score(0)
        ball.reset()

    elif ball.xcor() < -350:
        ball.reset()
        score.score2 += 1
        score.increase_score(1)

screen.exitonclick()
