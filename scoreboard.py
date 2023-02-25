from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.goto(0, 270)
        self.hideturtle()
        self.color("White")
        self.update_score()

    def update_score(self):
        self.write(f"{self.score1} : {self.score2} ", False, "center", ("Courier", 35, "normal"))

    def increase_score(self, player):
        if player == "1":
            self.score1 += 1
        elif player == "0":
            self.score2 += 1
        self.clear()
        self.update_score()

    def check_winner(self):
        if self.score1 == 1:
            self.goto(0, 0)
            self.write(f"Game over Plater 1 wins", False, "center", ("Courier", 35, "normal"))
            return False
        elif self.score2 == 1:
            self.goto(0, 0)
            self.write(f"Game over Plater 2 wins", False, "center", ("Courier", 35, "normal"))
            return False

