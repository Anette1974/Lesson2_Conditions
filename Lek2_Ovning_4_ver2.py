# Veckouppgift 2, Övning 4 (version 2)
'''4 Temperaturomvandling
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
Version 1, exempel på output:

Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.

Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen.
Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i i Fahrenheit. Använd sedan if + else.

Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder. Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

Formel för konvertering mellan temperaturenheter:
C = (F - 32) / 1.8
F = 1.8 * C + 32
'''
print("Veckouppgift 2, Övning 4 (version 2)")
temp_choice = (input("Vill du omvandla från Celsius->Fahrenheit, skriv C. Om du vill omvandla från Fahrenheit->Celsius, skriv F: "))
print(f"Du valde att konvertera från {temp_choice}.")
#while True:
#   if temp_choice == "c" or temp_choice == "C" or temp_choice == "f" or temp_choice == "F":
#        break
#    else:
#        print("Du har gjort ett felaktigt val!")
#Fick hjälp av AI att göra en fungerande while sats
while temp_choice not in ['c', 'C', 'f', 'F']:
    print("Du har gjort ett felaktigt val!")
    temp_choice = input("Vill du omvandla från Celsius->Fahrenheit, skriv C. Om du vill omvandla från Fahrenheit->Celsius, skriv F: ")
if temp_choice in ['c', 'C']:
    #temp_choice == "c" or temp_choice == "C": # Bättre förslag från AI
    celsius_degree = float(input("Ange grader i Celcius: "))
    fahr_conv_celc = 1.8 * celsius_degree + 32  # Formel för konvertering från Celsius till Fahrenheit
    print(f"Det blir {fahr_conv_celc} grader Fahrenheit")

elif temp_choice in ['f', 'F']:
    #temp_choice == "f" or temp_choice == "F": # bättre förslag från AI
    fahrenheit_degree = float(input("Ange grader i Fahrenheit: "))
    cels_conf_fahr = (fahrenheit_degree - 32) / 1.8  # Formel för konvertering från Fahrenheit till Celsius
    print(f"Det blir {cels_conf_fahr} grader Celsius")
