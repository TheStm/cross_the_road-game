from turtle import Turtle
import random
import scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self, lvl):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(x=300, y=random.randrange(-250, 285,20))
        self.shapesize(stretch_len=2)
        self.lvl = lvl

    def move(self):
        self.setx(self.xcor() - (STARTING_MOVE_DISTANCE + (self.lvl - 1) * MOVE_INCREMENT))

    def lvl_up(self):
        self.lvl += 1