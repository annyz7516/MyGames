
from turtle import Turtle, Screen

screen = Screen()
instruction = Turtle
ted = Turtle()
ted.color("pink")
ted.shape("turtle")

nat = Turtle()
nat.color("blue")
nat.shape("turtle")

ben = Turtle()
ben.color("orange")
ben.shape("turtle")


def ted_forwards():
    ted.forward(10)

def nat_forwards():
    nat.forward(10)

def ben_forwards():
    ben.forward(10)

#aset start line
ted.right(90)
ted.penup()
ted.forward(100)
ted.right(90)
ted.forward(500)
ted.right(180)

nat.right(180)
nat.penup()
nat.forward(500)
nat.right(180)

ben.right(-90)
ben.penup()
ben.forward(100)
ben.right(-90)
ben.forward(500)
ben.right(180)

screen.listen()
screen.onkey(key="l", fun=ted_forwards)
screen.onkey(key="d", fun=nat_forwards)
screen.onkey(key="n", fun=ben_forwards)

screen.exitonclick()
