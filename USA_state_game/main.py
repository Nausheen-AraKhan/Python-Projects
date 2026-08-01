import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 states Correct",prompt="Enter a state").title()
    if answer_state=="Exit":
        miss_states=[]
        for state in all_states:
            if state not in guessed_state:
                miss_states.append(state)
        new_data=pandas.DataFrame(miss_states)
        new_data.to_csv("miss_states.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())
