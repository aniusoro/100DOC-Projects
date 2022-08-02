from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_on = True
while game_on:
  time.sleep(0.1)
  screen.update()
  ball.move()
  
  #detect collision with wall
  if ball.ycor > 280 or ball.ycor < -280:
    ball.bounce()
    
  #detect collision with right paddle
  #checking if balll has gone far enough enough to be part of the paddle and its within a distance of 50 pixels
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    
  #detect when right paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()
    
  #left side paddle miss
  if ball.xcor() < -380:
    ball.reset_position
    scoreboard.r_point()

screen.exitonclick()
