import turtle as t
t.speed(0)
t.bgcolor("black")
t.pencolor("yellow")
for i in range(300):
    t.rt(i)
    t.circle(100,i)
    t.fd(i)
    t.lt(90)
t.done()

# 2
for i in range(36):
    for i in range(36):
        go(10)
        turn(10)
    turn(10)

# 3
def circle():
    for i in range(36):
        go(10)
        turn(10)

color_list=["red", ]  # write total 6 colors
for item in color_list:
    color(item)
    circle()
    turn(60)