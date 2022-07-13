from turtle import Turtle
COORDINATES1 = [(350, 0), (350, 20), (350, 40)]
COORDINATES2 = [(-350, 0), (-350, 20), (-350, 40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle1():

    def __init__(self):
        self.segment1 = []
        self.create_paddle1()
        self.head = self.segment1[0]

    def create_paddle1(self):
        for position in COORDINATES1:
            self.add_segment(position)

    def add_segment(self, position):
        paddle = Turtle(shape="square")
        paddle.color("white")
        paddle.penup()
        paddle.goto(position)
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.segment1.append(paddle)


class Paddle2():
    def __init__(self):
        self.segment2 = []
        self.create_paddle2()
        self.head = self.segment2[0]

    def create_paddle2(self):
        for position in COORDINATES2:
            self.add_segment(position)

    def add_segment(self, position):
        paddle = Turtle(shape="square")
        paddle.color("white")
        paddle.penup()
        paddle.goto(position)
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.segment2.append(paddle)

