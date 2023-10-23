#imports
from turtle import Turtle , Screen
import pandas

screen=Screen()
tim=Turtle()


image="blank_states_img.gif"




screen.title("U.S. States Game")

#adding the image that we want to write on it !
screen.addshape(image)

tim.shape(image)


guessed_states=[]

#keep questioning the user of the states as they are not completed yet , unless he exits the game !
while len(guessed_states)<50:
  answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="whats another state's name?").title()


  data=pandas.read_csv("50_states.csv")
  all_states=data.state.to_list()
   
   #if the user press exit , even if he writed the 50 state , then we will count the wrong state as a missed state 
   # and add it to states to learn!,
  if answer_state=="Exit":
    missing_states=[state for state in all_states if state not in guessed_states]
    newdata=pandas.DataFrame(missing_states)
    newdata.to_csv("States to learn.csv")
        
    break
  
  #check if answer_state is one of the states inside ythe csv
  #what we are doing here is if he types a correct state 
  # then the text will go to that state according to its coordinates in the csv which is related to the picture !
  if answer_state in all_states:
    guessed_states.append(answer_state)
    tim.hideturtle()
    tim.penup()
    statedata=data[data.state==answer_state]
    tim.goto(int(statedata.x,statedata.y))
    tim.write(answer_state)
    #or tim.write(statedata.state.item()) which extracts the noise and just give you the item !

    