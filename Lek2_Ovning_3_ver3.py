# Veckouppgift 2, Övning 3 (version 3)
'''
Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
Exempel på output:

Matchen är över, nu ska vi räkna ut resultatet!
Hur många mål gjorde Tottenham? 2
Hur många mål gjorde Liverpool? 1
Tottenham vann!

Version 2: programmet ska tala om ifall det blev oavgjort.

Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
Tottenham vann med 1 mål!

Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.
'''
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