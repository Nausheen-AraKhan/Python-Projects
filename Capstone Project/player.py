from turtle import Turtle
STARTING_POS=(0,-280)
MOVING_STEPS=10
FINISH_LINE=280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_starting_pos()
        self.setheading(90)
    def move_up(self):
        self.forward(MOVING_STEPS)
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False
    def go_to_starting_pos(self):
        self.goto(STARTING_POS)
