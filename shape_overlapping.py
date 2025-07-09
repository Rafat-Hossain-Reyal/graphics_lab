import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(3)

pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
pen.circle(50)
pen.end_fill()


pen.penup()
pen.goto(-60, -60)
pen.pendown()
pen.color("green")
pen.begin_fill()
for _ in range(4):
    pen.forward(120)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(0, -120)
pen.pendown()
pen.color("magenta")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

pen.hideturtle()
screen.mainloop()