# Veckouppgift 2, Övning 3 (version 3)
print("Veckouppgift 2, Övning 3 (version 3)")
tottenham_goal = int(input("Hur många mål gjorde Tottenham? "))
liverpool_goal = int(input("Hur många mål gjorde Liverpool? "))
if tottenham_goal > liverpool_goal:
    goal_difference = tottenham_goal-liverpool_goal
    print (f"Tottenhamn vann med {goal_difference} mål!")
elif liverpool_goal > tottenham_goal:
    goal_difference = liverpool_goal - tottenham_goal
    print (f"Liverpool vann med {goal_difference} mål!")
else:
    print(f"Det blev oavgjort {tottenham_goal} - {liverpool_goal}")