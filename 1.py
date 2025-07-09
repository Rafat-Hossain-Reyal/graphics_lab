import turtle
import time

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("blue")

screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(0)

x = -300
while True:
    t.clear()
    t.goto(x, 0)
    t.write("Reyal", font=("Arial", 24, "bold"))
    x += 2
    if x > 300:
        x = -300
    screen.update()
    time.sleep(0.01)
