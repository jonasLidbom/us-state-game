import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)  # Adds an image as shape. Turtle only accepts gif.
turtle.shape(img)

data = pandas.read_csv("50_states.csv") # Reads the 50_states.csv.
all_states = data.state.to_list() # Converts the data["state"] to a list with only states.
correct_guesses = []  # List that will contain the correct guesses,

while len(correct_guesses) < 50:  # Game continues until you have guessed every state right.
    # Text input that saves the users guess.
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(all_states)} States Correct", prompt="What's another state's name?").title()
    # If the user guess "Exit": Saves the missing states into a new csv and breaks the loop.
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # If the answer is correct, saves the state into correct_guesses and creates turtle that writes
    # the state name on the screen.
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y)) # Gets the x and y attribute from state_data row.
        t.write(arg=answer_state, align="center", font=('Arial', 8, 'normal'))  # Writes the name of the guessed state.
        correct_guesses.append(answer_state)



