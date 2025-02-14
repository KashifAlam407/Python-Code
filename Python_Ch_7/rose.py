import turtle

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.color("red")
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

# Draw a rose using the polar equation of a rose curve
for i in range(360):
    theta = i * 0.1
    x = 300 * (1 - 0.9 * theta) * turtle.cos(theta)
    y = 300 * (1 - 0.9 * theta) * turtle.sin(theta)
    turtle.goto(x, y)

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
