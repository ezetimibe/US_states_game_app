import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US Game Practice")
image = "blank_states_img.gif"
screen.bgpic("blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_file = data.state.to_list()
all_state = []
remaining_state = []
while len(all_state) < 50:
    answer_state = screen.textinput(title=f"{len(all_state)}/50", prompt="Enter a US state name").title()
    if answer_state == "Exit":
        for state in data_file:
            if state not in all_state:
                remaining_state.append(state)
        print(f"{len(remaining_state)} {remaining_state}")
        new_data = pandas.DataFrame(remaining_state)
        print(new_data)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in data_file:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(arg=answer_state)
        all_state.append(answer_state)

# screen.exitonclick()