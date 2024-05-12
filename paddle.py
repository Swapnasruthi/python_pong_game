import turtle as t

class Paddle:
    def __init__(self,x_cor,y_cor):
        self.paddle = t.Turtle(shape="square")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(x_cor, y_cor)

    def paddle_up(self):
        new_ycor = self.paddle.ycor() + 40
        self.paddle.goto(self.paddle.xcor(), new_ycor)

    def paddle_down(self):
        new_ycor = self.paddle.ycor() - 40
        self.paddle.goto(self.paddle.xcor(), new_ycor)