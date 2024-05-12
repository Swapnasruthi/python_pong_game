from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x=10
        self.y=10
    def move(self):
        x_cor=self.xcor()+self.x
        y_cor=self.ycor()+self.y
        self.goto(x_cor,y_cor)
    def bounce(self):
        self.y *= -1
    def paddle_bounce(self):
        self.x *= -1

    def reset_position(self):
        self.goto(0,0)
        self.paddle_bounce()