from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            random_length = random.randint(2, 4)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=random_length)
            new_car.setheading(180)
            new_car.penup()
            #change color
            new_car.color(random.choice(COLORS))
            #chang start_position:
            y = random.randint(-230, 250)
            new_car.goto(280, y)
            self.all_cars.append(new_car)

    def move_cars(self, level):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + level*MOVE_INCREMENT)

    def reset(self):
        self.clear()



