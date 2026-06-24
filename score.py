
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore= self.get_highscore()
        self.color("red")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.ubdate_scoreboard()


    def get_highscore(self):
        with open("highscore.txt","r") as file:
            return int(file.read())
        

    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))



    def ubdate_scoreboard(self):
        self.write(f"score: {self.score}   High score: {self.highscore}", align="center", font=("Arial", 20, "normal"))
        

    def increase_score(self):
        self.score+=1
        self.clear()
        self.ubdate_scoreboard()


    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore=self.score
            self.save_highscore()
        self.write(f" ------- Game over ------- \n \n     Final score: {self.score} \n \n     High score: {self.highscore}", align="center", font=("Arial",20,"normal"))
        self.hideturtle()

