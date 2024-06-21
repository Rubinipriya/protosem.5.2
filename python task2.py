import turtle

# Initialize the turtle
t = turtle.Turtle()
t.speed(3)

# Function to draw a circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw the body
draw_circle("brown", 50, 0, -50)

# Draw the head
draw_circle("brown", 30, 0, 50)

# Draw the ears
draw_circle("brown", 10, -25, 90)
draw_circle("brown", 10, 25, 90)

# Draw the inner ears
draw_circle("pink", 5, -25, 95)
draw_circle("pink", 5, 25, 95)

# Draw the eyes
draw_circle("black", 5, -10, 65)
draw_circle("black", 5, 10, 65)

# Draw the nose
draw_circle("black", 3, 0, 55)

# Draw the mouth
t.penup()
t.goto(-5, 50)
t.pendown()
t.right(90)
t.circle(5, 180)
t.penup()
t.goto(5, 50)
t.pendown()
t.circle(5, -180)

# Draw the bowtie
t.penup()
t.goto(-10, 40)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10, 180)
t.left(90)
t.forward(10)
t.left(90)
t.circle(10, 180)
t.left(90)
t.forward(10)
t.end_fill()

t.penup()
t.goto(10, 40)
t.pendown()
t.begin_fill()
t.circle(10, -180)
t.left(90)
t.forward(10)
t.left(90)
t.circle(10, -180)
t.left(90)
t.forward(10)
t.end_fill()

# Draw the arms
t.penup()
t.goto(-50, 0)
t.pendown()
t.circle(50, 90)
t.penup()
t.goto(50, 0)
t.pendown()
t.circle(-50, 90)

# Draw the legs
t.penup()
t.goto(-30, -50)
t.pendown()
t.circle(30, 90)
t.penup()
t.goto(30, -50)
t.pendown()
t.circle(-30, 90)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
