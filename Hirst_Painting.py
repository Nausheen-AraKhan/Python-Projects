import turtle as t
import random

t.colormode(255)
tim=t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

color_list=[(238, 224, 203), (204, 157, 106), (172, 71, 36), (233, 216, 224), (217, 218, 226), (227, 208, 117), (141, 145, 160), (95, 104, 135), (192, 151, 170), (183, 152, 41), (223, 229, 224), (32, 34, 14), (19, 26, 61), (97, 115, 173), (221, 172, 195), (173, 28, 9), (22, 36, 20), (121, 105, 113), (197, 98, 74), (234, 174, 160), (144, 151, 146), (101, 109, 103), (41, 51, 100), (182, 184, 214), (172, 104, 122), (46, 29, 45), (73, 72, 41), (232, 203, 16), (121, 38, 50), (55, 71, 54)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_dots=100
for dot_count in range(1,no_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen=t.Screen()
screen.exitonclick()
