import pandas as pd
from drawer import Drawer
import turtle
tim= Drawer()
screen= turtle.Screen()
screen.title("US states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("50_states.csv")
guessed =[]
missing_states=[]
while len(guessed)<50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 Guessed Correctly", prompt="input state name")
    answer_state=answer_state.title()
    if answer_state == "Exit":
        missing_states=[x for x in data.state.to_list() if x not in guessed]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    result = False
    for x in guessed:
        if answer_state == x:
            result = True
        #We can access a column by the name.the_column we wnat
    if answer_state in data.state.to_list() and result == False:
        # This is how you extract a row of data from a column,
        state_data = data[data["state"] == answer_state]
        guessed.append(answer_state)
        tim.move(int(state_data.x),int(state_data.y),answer_state)
        #The .values attribute of a Series returns a NumPy array containing the values of the Series.
        # This is useful for converting the Series to a more manageable form, especially when you know there's
        # only one value you care about
# states to learn csv

screen.exitonclick()