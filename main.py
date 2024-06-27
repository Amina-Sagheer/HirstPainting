import random
import colorgram
import turtle as t

rgb_values = []
t.colormode(255)
colors = colorgram.extract('img.png', 16)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_values.append(new_color)
timmy = t.Turtle()
timmy.shape('turtle')
timmy.penup()
timmy.goto(-100, 100)

for row in range(10):
    for col in range(10):
        timmy.color(random.choice(rgb_values))
        timmy.dot(10)
        timmy.penup()
        timmy.forward(20)
    timmy.backward(20 * 10)
    timmy.right(90)
    timmy.forward(20)
    timmy.left(90)

timmy.hideturtle()

my_screen = t.Screen()
my_screen.exitonclick()
