import turtle
import pandas

data = pandas.read_csv('50_states.csv')
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
all_states = data['state'].to_list()
missing_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data['state'] == answer_state]
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(int(state_data['x']), int(state_data['y']))
        timmy.write(answer_state)


