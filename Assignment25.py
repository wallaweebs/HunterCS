#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import turtle

tess = turtle.Turtle()
trtl = turtle.Screen()     #The graphics window
inpt = input("Please enter a command string: ")

for ch in inpt:
    if(ch == "F"):
        tess.forward(50)
    elif(ch == "L"):
        tess.left(90)
    elif(ch == "R"):
        tess.right(90)
    elif(ch == "^"):
        tess.penup()
    elif(ch == "v"):
        tess.pendown()
    elif(ch == "B"):
        tess.backward(50)
    elif(ch == "S"):
        tess.stamp()
    elif(ch == "l"):
        tess.left(45)
    elif(ch == "r"):
        tess.right(45)
    elif(ch == "p"):
        tess.color("purple")
    else:
        print("Input correct letters!")

trtl.exitonclick()