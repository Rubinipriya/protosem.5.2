import turtle

# Initialize the turtle
t = turtle.Turtle()
t.speed(3)

# Function to draw a rectangle
def draw_rectangle(color, width, height, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a triangle
def draw_triangle(color, base, height, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(base)
    t.left(135)
    t.forward(height)
    t.left(90)
    t.forward(height)
    t.left(135)
    t.end_fill()

# Draw the church body
draw_rectangle("lightgray", 100, 150, -50, -150)

# Draw the church roof
draw_triangle("darkgray", 120, 85, -60, 0)

# Draw the church door
draw_rectangle("brown", 30, 50, -15, -150)

# Draw windows
draw_rectangle("white", 20, 30, -40, -50)
draw_rectangle("white", 20, 30, 20, -50)

# Draw the cross on top
t.penup()
t.goto(-5, 85)
t.pendown()
t.pencolor("black")
t.pensize(3)
t.left(90)
t.forward(20)
t.backward(10)
t.left(90)
t.forward(10)
t.backward(20)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
