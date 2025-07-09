import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Realistic Starfield View")
screen.setup(width=800, height=600)
screen.tracer(0)

# Star class for 3D movement
class Star:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.uniform(-400, 400)
        self.y = random.uniform(-300, 300)
        self.z = random.uniform(1, 800)
        self.pz = self.z
        self.color = random.choice(["white", "lightblue", "yellow", "lightgray"])

    def update(self, speed):
        self.pz = self.z
        self.z -= speed
        if self.z <= 1:
            self.reset()

    def draw(self, t):
        # Convert 3D to 2D perspective
        sx = int(self.x / self.z * 800)
        sy = int(self.y / self.z * 800)
        px = int(self.x / self.pz * 800)
        py = int(self.y / self.pz * 800)

        # Calculate star size
        size = max(1, int((800 - self.z) / 100))

        # Draw star trail
        t.pencolor(self.color)
        t.pensize(size / 2)
        t.goto(px, py)
        t.pendown()
        t.goto(sx, sy)
        t.penup()

# Turtle setup
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

# Create starfield
stars = [Star() for _ in range(150)]

# Animation loop
while True:
    t.clear()
    for star in stars:
        star.update(speed=10)
        star.draw(t)
    screen.update()
