import turtle as t
import random

sam = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


sam.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        sam.color(random_color())
        sam.circle(100)
        sam.setheading(sam.heading() + size_of_gap)
        sam.circle(100)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
