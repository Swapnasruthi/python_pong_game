import turtle as t
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = t.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.listen()
screen.tracer(0)

score_board=ScoreBoard()
L_paddle=Paddle(350,0)
R_paddle=Paddle(-350,0)
ball=Ball()


screen.onkey(L_paddle.paddle_up,"Up")
screen.onkey(L_paddle.paddle_down,"Down")
screen.onkey(R_paddle.paddle_up,"w")
screen.onkey(R_paddle.paddle_down,"s")

tim=t.Turtle()
tim.penup()
tim.setheading(270)
tim.fd(300)
tim.setheading(90)
tim.pensize(5)
for i in range(1,100):
    tim.pendown()
    tim.color("white")
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.03)
    ball.move()

    #detecting collision with the walls by ball
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    #detecting collision with the paddles by ball
    if ball.distance(L_paddle.paddle)<50 and ball.xcor()>330 or ball.distance(R_paddle.paddle)<50 and ball.xcor()<-330:
        ball.paddle_bounce()


    #detect L paddle misses
    if ball.xcor()>380:
        score_board.l_increase()
        ball.reset_position()

     #detect R paddle misses

    if ball.xcor() < -380:
        score_board.r_increase()
        ball.reset_position()



screen.exitonclick()