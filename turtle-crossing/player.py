from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize()
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0, -290)
        #self.refresh()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def move_right(self):
        self.right(90)
        self.forward(10)
        self.right(-90)

    def move_left(self):
        self.right(-90)
        self.forward(10)
        self.right(90)


