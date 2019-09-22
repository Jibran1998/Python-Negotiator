#Negotiator-> Negottiates the budget
from speaker import speak

profit_percentage = 10
projectcost2=1

#For negotiation of the cost the compromisation part
def negotiation(user):
    global projectcost1
    global projectcost2
    global profit_percentage
    while True:
        print("Bot: Select a feature on which you can compromise")
        print("a: Quality")
        print("b: Timeline")
        speak("Bot: Select a feature on which you can compromise\na: Quality\nb: Timeline")
        query = input(f"{user}: ")
        ####query=takeCommand()
        # print(f"{user}: query")
        if query.lower() in ('a','b'):
            break

    compromise = query
    if "a" in compromise:
        projectcost2 = projectcost1 * profit_percentage - 1
    elif "b" in compromise:
        projectcost2 = projectcost1 * profit_percentage - 2
    while True:
        print(f"Bot: According to my analysis your budget is {int(projectcost2)}, Do you agree?")
        speak(f"According to my analysis your budget is {int(projectcost2)}K rupees, Do you agree?")
        query = input(f"{user}: ")
        ####query=takeCommand()
        # print(f"{user}: query")
        if query.lower() in ('yes','no'):
            break

    if "yes" in query:
            projectcost1=projectcost2
            return True
    profit_percentage = profit_percentage - 1

#decides the cost of the project
def decider(projectCost,user):
    global projectcost1
    projectcost1= projectCost
    global profit_percentage
    profit_percentage=10
    i = 1
    while i<=5:
        if negotiation(user):
            print(projectcost1)
            i=7
        else:
            i = i + 1
    #Negotiation failed
    if i==6:
        return False,projectcost2
    return True,projectcost1
