import time
from turtle import Turtle, Screen
from snake import Snake
from bean import Bean
from scoreboard import Scoreboard

with open("data.txt") as file:
    new_high_score = file.read()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
bean = Bean()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(bean) < 20:
        bean.refresh()
        score.increase_score()
        snake.extend()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            score.reset()
            snake.reset()
        game_is_on = True


    #Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        #game_is_on = False
        score.reset()
        snake.reset()
    game_is_on = True












screen.exitonclick()
