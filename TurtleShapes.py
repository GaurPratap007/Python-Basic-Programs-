import turtle as t
import random

tur = t.Turtle()
colours = ["Green", "Red", "Blue", "Yellow", "Pink", "Brown"]
tur.speed("fastest")
screen = t.Screen()
screen.exitonclick()


def draw_sharpe(sides):
    angle = 360/sides
    for i in range(sides):
        tur.forward(100)
        tur.right(angle)


def all_shapes():
    for shape in range(3,11):
        tur.color(random.choice(colours))
        draw_sharpe(shape)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(gap):
    for _ in range (int(360/gap)):
        tur.color(random.choice(colours))
        tur.circle(100)
        tur.setheading(tur.heading() + gap)


spirograph(5)