import turtle

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("lightblue")

# Draw the body of the parrot
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

# Draw the head of the parrot
turtle.penup()
turtle.goto(-180, 80)
turtle.pendown()
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

# Draw the beak of the parrot
turtle.penup()
turtle.goto(-140, 80)
turtle.pendown()
turtle.color("orange")
turtle.begin_fill()
turtle.goto(-120, 50)
turtle.goto(-100, 80)
turtle.end_fill()

# Draw the eye of the parrot
turtle.penup()
turtle.goto(-160, 100)
turtle.pendown()
turtle.color("black")
turtle.dot(20)

# Draw the wings of the parrot
turtle.penup()
turtle.goto(-60, 20)
turtle.pendown()
turtle.right(20)
turtle.circle(100, 90)
turtle.right(20)
turtle.circle(100, 90)

# Draw the tail of the parrot
turtle.penup()
turtle.goto(-20, -80)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.right(120)
turtle.circle(80, 180)
turtle.end_fill()

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
