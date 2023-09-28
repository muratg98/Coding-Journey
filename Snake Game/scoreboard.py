from turtle import Turtle

SCORE = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.high_score = 0
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {SCORE}", align='center', font=('Arial', 12, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Arial', 12, 'bold'))

    def update_score(self):
        global SCORE
        SCORE += 1
        self.clear()
        self.write(f"Score: {SCORE}", align='center', font=('Arial', 12, 'bold'))
