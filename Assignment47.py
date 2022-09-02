#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import turtle
import random

trtl = turtle.Turtle()

for i in range(100):
    trtl.forward(10)
    degrees = random.randrange(0, 360, 90)
    trtl.right(degrees)
