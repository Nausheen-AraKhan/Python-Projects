from email import message
from tkinter import messagebox
from turtle import Turtle, Screen
import random
is_race_on=False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title= "Make a bet", prompt="Choose the turtle color!")
colors=["red","pink","blue","green","purple","goldenrod"]
y_pos=[-125,-85,-45,-5,35,75]
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_pos[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle  in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user_bet:
                messagebox.showinfo("Winner","You win!")
                print(f"You won! {winning_turtle} color turtle won")
            else:
                messagebox.showinfo("Lost","You lose!")
                print(f"You lost! {winning_turtle} color turtle won")
        random_dist=random.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()
