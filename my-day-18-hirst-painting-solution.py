# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle as t
import random

color_list = [(254, 253, 252), (232, 254, 243), (253, 234, 245), (43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253),
(160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251),
(211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171),
(16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205),
(204, 119, 35), (112, 6, 4)]

t.colormode(255)
ani = t.Turtle()


def find_space():
    ani.setheading(225)
    ani.penup()
    ani.forward(300)
    ani.pendown()
    ani.setheading(0)

def movement(steps):
    for i in range(steps):
        ani.dot(20, random.choice(color_list))
        ani.penup()
        ani.forward(50)
        ani.pendown()
        ani.dot(20, random.choice(color_list))


def left_rotation():
    ani.left(90)
    ani.penup()
    ani.forward(50)
    ani.pendown()
    ani.left(90)
    ani.dot(20, random.choice(color_list))
    ani.penup()
    ani.forward(50)
    ani.pendown()
    ani.dot(10, random.choice(color_list))


def right_rotation():
    ani.right(90)
    ani.penup()
    ani.forward(50)
    ani.pendown()
    ani.right(90)
    ani.dot(20, random.choice(color_list))
    ani.penup()
    ani.forward(50)
    ani.pendown()
    ani.dot(20, random.choice(color_list))


ani.hideturtle()
find_space()
ani.speed("fastest")
movement(9)
for i in range(5):
    left_rotation()
    movement(8)
    right_rotation()
    movement(8)


screen = t.Screen()
screen.exitonclick()