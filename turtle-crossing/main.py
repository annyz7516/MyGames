import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from train import TrainManager
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

start_game = screen.textinput(title="CROSSY TURTLE",
                            prompt="START OR QUIT:")

if start_game.lower() == "start":
    game_is_on = True
else:
    screen.exitonclick()

turtle = Player()
screen.listen()

cars = CarManager()
cars.create_car()

trains = TrainManager()



level = 0

screen.onkeypress(turtle.move_up, "Up")
screen.onkeypress(turtle.move_down, "Down")
screen.onkeypress(turtle.move_right, "Right")
screen.onkeypress(turtle.move_left, "Left")

score = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars(level)

    trains.create_car()
    trains.move_cars(level)

    #check collision with cars
    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            score.game_over()
            game_is_on = False
            #restart function( BUG!!! )as followed
            turtle.goto(0, -290)
            # restart_game = screen.textinput(title="GAME OVER",
            #                               prompt="RESTART OR QUIT:")
            # if restart_game.lower() == "restart":
            #     game_is_on = True
            #     turtle.goto(0, -290)
            #     cars.reset()
            # else:
            #     game_is_on = False

        if turtle.ycor() == 280:
            score.increase_score()
            turtle.goto(0, -290)
            level += 1

    for car in trains.all_cars:
        if turtle.distance(car) < 30:
            score.game_over()
            game_is_on = False
            turtle.goto(0, -290)
            # restart_game = screen.textinput(title="GAME OVER",
            #                                 prompt="RESTART OR QUIT:")
            # if restart_game.lower() == "restart":
            #     game_is_on = True
            #     screen.update()
            #     turtle.goto(0, -290)
            #     trains.reset()
            # else:
            #     game_is_on = False

        if turtle.ycor() == 280:
            score.increase_score()
            turtle.goto(0, -300)
            level += 1

    if turtle.xcor() > 280 or turtle.xcor() < -280:
        score.game_over()
        game_is_on = False

    # if restart_game.lower() == "restart":
    #     game_is_on = True






screen.exitonclick()