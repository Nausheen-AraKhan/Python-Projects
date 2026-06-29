from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)
def go_left():
    tim.left(10)
def go_right():
    tim.right(10)
def go_back():
    tim.backward(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=go_back())
screen.onkey(key="d",fun=go_left)
screen.onkey(key="a",fun=go_right)
screen.onkey(key="q",fun=clear_screen)
screen.exitonclick()
