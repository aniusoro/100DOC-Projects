from turtle import Turtle, Screen
from Paddle import Paddle1, Paddle2
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
P1 = Paddle1()
P2 = Paddle2()
scoreboard1 = Scoreboard()
screen.update()


screen.exitonclick()
