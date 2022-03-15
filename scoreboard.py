from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.write("Score: ", False, align="center", font=("Arial", 8, "normal"))
        self.color("white")

