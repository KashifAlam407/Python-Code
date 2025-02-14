import turtle

# Set up the turtle
turtle.speed(5)
turtle.bgcolor("lightblue")

# Draw the body of the parrot
turtle.penup()
turtle.goto(-40, -100)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

# Draw the head of the parrot
turtle.penup()
turtle.goto(-80, -20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# Draw the beak of the parrot
turtle.penup()
turtle.goto(-65, -20)
turtle.pendown()
turtle.color("orange")
turtle.begin_fill()
turtle.goto(-55, -20)
turtle.goto(-65, -30)
turtle.end_fill()

# Draw the eye of the parrot
turtle.penup()
turtle.goto(-85, 0)
turtle.pendown()
turtle.color("black")
turtle.dot(10)

# Draw the wings of the parrot
turtle.penup()
turtle.goto(-40, -60)
turtle.pendown()
turtle.right(20)
turtle.circle(50, 90)
turtle.right(20)
turtle.circle(50, 90)

# Draw the tail of the parrot
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.left(120)
turtle.circle(40, 180)
turtle.end_fill()

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
