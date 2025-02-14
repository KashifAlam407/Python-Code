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

# Move to write "I love you"
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

# Write "I love you"
turtle.color('black')
turtle.write("I love you", font=("Arial", 20, "normal"))

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
