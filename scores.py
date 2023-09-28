from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", align='center', font=('Arial', 25, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align='center', font=('Arial', 25, 'bold'))
