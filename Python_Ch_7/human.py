import turtle

# Set up the turtle
turtle.speed(0)  # Set the fastest drawing speed
turtle.penup()
turtle.goto(0, -200)  # Start drawing from the bottom center of the screen
turtle.pendown()

# Draw the outline of a simple human-like shape
turtle.fillcolor('black')  # Set the fill color to black
turtle.begin_fill()  # Start filling the shape
turtle.circle(50)  # Head
turtle.forward(100)  # Body
turtle.left(90)
turtle.forward(80)  # Left leg
turtle.backward(160)  # Right leg
turtle.forward(80)  # Go back to the body
turtle.left(90)
turtle.forward(40)  # Left arm
turtle.backward(80)  # Right arm
turtle.end_fill()  # Finish filling the shape

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
