from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
GAME_OVER_FONT = ("Arial", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)

    def score_increment(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
