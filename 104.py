# Create an Equilateral Triangle, Rectangle, and Hexagon using Turtle

import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Shapes")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)

# Draw Equilateral Triangle
pen.fillcolor("yellow")
pen.begin_fill()
for i in range(3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()

# Move to a new position
pen.penup()
pen.goto(-150, -150)
pen.pendown()

# Draw Rectangle
pen.fillcolor("green")
pen.begin_fill()
for i in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()

# Move to a new position
pen.penup()
pen.goto(150, -50)
pen.pendown()

# Draw Hexagon
pen.fillcolor("red")
pen.begin_fill()
for i in range(6):
    pen.forward(70)
    pen.left(60)
pen.end_fill()

# Hide turtle and keep window open
pen.hideturtle()
turtle.done()