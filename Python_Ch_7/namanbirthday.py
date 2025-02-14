import turtle

# Function to draw a letter 'N'
def draw_N():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(140)
    turtle.left(135)
    turtle.forward(100)

# Function to draw a letter 'A'
def draw_A():
    turtle.left(75)
    turtle.forward(200)
    turtle.right(150)
    turtle.forward(200)
    turtle.backward(100)
    turtle.right(105)
    turtle.forward(67)
    turtle.backward(67)

# Function to draw a letter 'M'
def draw_M():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(150)
    turtle.forward(120)
    turtle.left(120)
    turtle.forward(120)
    turtle.right(150)
    turtle.forward(100)

# Function to draw a letter 'B'
def draw_B():
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.circle(-50,180)
    turtle.right(180)
    turtle.circle(-50,180)
    turtle.penup()
    turtle.goto(50,100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(150)

# Function to draw a letter 'I'
def draw_I():
    turtle.forward(10)
    turtle.backward(5)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(5)

# Function to draw a letter 'R'
def draw_R():
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.circle(-50,180)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

# Function to draw a letter 'T'
def draw_T():
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(100)

# Function to draw a letter 'H'
def draw_H():
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(200)

# Function to draw a letter 'D'
def draw_D():
    turtle.left(90)
    turtle.forward(200)
    turtle.circle(-50,180)
    turtle.backward(200)

# Function to draw a letter 'Y'
def draw_Y():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(70)
    turtle.backward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.backward(70)

# Set up the turtle
turtle.speed(1)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# Drawing the name "NAMAN BIRTHDAY"
draw_N()
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
draw_A()
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
draw_M()
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()
draw_A()
turtle.penup()
turtle.goto(450, 0)
turtle.pendown()
draw_N()
turtle.penup()
turtle.goto(600, 0)
turtle.pendown()
draw_B()
turtle.penup()
turtle.goto(750, 0)
turtle.pendown()
draw_I()
turtle.penup()
turtle.goto(800, 0)
turtle.pendown()
draw_R()
turtle.penup()
turtle.goto(950, 0)
turtle.pendown()
draw_T()
turtle.penup()
turtle.goto(1050, 0)
turtle.pendown()
draw_H()
turtle.penup()
turtle.goto(1250, 0)
turtle.pendown()
draw_D()
turtle.penup()
turtle.goto(1450, 0)
turtle.pendown()
draw_A()
turtle.penup()
turtle.goto(1600, 0)
turtle.pendown()
draw_Y()

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
