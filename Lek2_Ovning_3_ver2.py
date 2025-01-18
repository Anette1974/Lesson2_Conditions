# Veckouppgift 2, Övning 3 (version 2)
print("Veckouppgift 2, Övning 3, version 2")
tottenham_goal = int(input("Hur många mål gjorde Tottenham? "))
liverpool_goal = int(input("Hur många mål gjorde Liverpool? "))
if tottenham_goal > liverpool_goal:
    print ("Tottenhamn vann!")
elif liverpool_goal > tottenham_goal:
    print ("Liverpool vann!")
else:
    print(f"Det blev oavgjort {tottenham_goal} - {liverpool_goal}")