from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


with open("data.txt") as file:
    new_high_score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.high_score = new_high_score
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        # self.write(f"score: {self.score}   Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}   Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()




