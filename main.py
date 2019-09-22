#main project file the project starts here

from textblob import TextBlob
from speaker import speak
import db_con
from listener import takeCommand
from negotiator import decider
import face

#setting intital cost and budget of the project
projectCost=0
budget=0
profit_percentage=10
#getting the costs of different platforms, timelines, and level of the programmer
def cost(ans):
    myresult = db_con.fetchData("info")
    for x in myresult:
        if str(x[0]) == str(ans):
            ans=x[1]
            return int(ans)
        else:
            pass


def result(reslt):
    if reslt:
        print("bot: Ok bye, I am on it!!")
        speak("Ok bye, I am on it!!")

    else:
        print("Bot: See you next Time :)")

def main():
    global budget
    global projectCost
    #getting the name from the camera
    name=face.getName()
    #if no face found
    if name.lower() == 'unknown':
        user="User"
        name_found=False
    else:
        #if face found
        user=name.capitalize()
        name_found=True
    #getting the questions
    myresult = db_con.fetchData("questions")

    #iterator for facial recognition to check the facae names
    j=1
    #asking the questions
    for x in myresult:
        if x[1] != None:
            choice = False
            while not choice:
                print(f"Bot:{x[0]}\n a:{x[1]}\n b:{x[2]}\n c:{x[3]}")
                speak(f"{x[0]}\na:{x[1]}\nb:{x[2]}\nc:{x[3]}")
                ans=input(f"{user}: ")
                ####ans=takeCommand()
                # print(f"{user}: ans")
                if ans.lower() in ('a','b','c'):
                    choice = True
            switcher = {
                "a": x[1],
                "b": x[2],
                "c": x[3],
            }
            ans = switcher.get(ans, "nothing")
            projectCost = projectCost + cost(ans)
        else:
            if name_found and j==1:
                ans=name
                print(f"Bot:Hi!! {name}")
                speak(f"Hi!!! {name}")
                j=j+1
            else:

                print(f"Bot: {x[0]}?")
                speak(f"{x[0]}?")
                ans=input(f"{user}: ")
                ####ans=takeCommand()
                # print(f"{user}: ans")
                blob = TextBlob(ans)
                if len(blob.noun_phrases) >0:
                    ans = blob.noun_phrases[0]
                ans = str(ans)
                if j==1:
                    face.addNew(ans)
                    j=j+1
        #saving the data in DataBase
        db_con.setData(name=x[0],value=ans)

    projectCost=projectCost*profit_percentage
    print(f"Bot: According to my analysis your budget is {projectCost}K rupees, Do you agree?")
    speak(f"According to my analysis your budget is {projectCost}k rupees, Do you agree?")
    while True:
        agreed=input(f"{user}: ")
        ####ans=takeCommand()
        # print(f"{user}: ans")
        if agreed.lower() in ('yes','no'):
            #deciding the buget if user dosent agreee
            if agreed.lower()=="no":
                state,budget=decider(projectCost/profit_percentage,user)
                if state==True:
                    db_con.setData("budget",budget)
                    result(state)
                    break
                if state == False:
                    result(state)
                    break
            elif agreed.lower() in "yes":
                result(True)
                break
        else:
            break
    budget=projectCost
    db_con.setData("budget", budget)


main()