import turtle
import pandas

FONT = ("Courier", 8, "normal")
IMAGE = "India.gif"

screen = turtle.Screen()
screen.title("India States Game")
screen.addshape(IMAGE)
screen.setup(width=720, height=845)
turtle.shape(IMAGE)

data = pandas.read_csv("india_36states.csv")
all_states = data["state"].tolist()
guessed_states = []

while len(guessed_states) < 36:
    answered_state = screen.textinput(title=f"{len(guessed_states)}/36 states correct",
                                      prompt="what's another state's name?").title()
    if answered_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]

        state_to_learn_df = pandas.DataFrame(missed_states)
        state_to_learn_df.to_csv("states_to_learn.csv")
        break

    if answered_state in all_states:
        if answered_state not in guessed_states:
            guessed_states.append(answered_state)

            state_name = turtle.Turtle()
            state_name.penup()
            state_name.hideturtle()
            x_pos = int(data[data["state"] == answered_state].x)
            y_pos = int(data[data["state"] == answered_state].y)
            state_name.goto(x_pos, y_pos)
            state_name.write(answered_state, font=FONT)
