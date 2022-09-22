from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 1
        self.penup()
        self.goto(-280, 260)
        self.write(f"LEVEL:{self.score}", font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"LEVEL:{self.score}", font=FONT)

    def update_scoreboard(self):
        self.write(f"LEVEL:{self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)






