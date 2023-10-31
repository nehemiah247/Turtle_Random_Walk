import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)
# colours = ['pale green', 'blue', 'dark green', 'red', 'pink', 'brown', 'Black', 'DeepSkyBlue', 'IndianRed',
#            'LightSeaGreen']
directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


random_color()

for i in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


