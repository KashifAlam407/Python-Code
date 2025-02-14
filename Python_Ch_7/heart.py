import turtle

# Function to draw a heart
def draw_heart():
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

# Set up the turtle
turtle.speed(2)
turtle.color('red')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Draw heart
draw_heart()

# Animate the heart beating
for _ in range(2):
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
