# Veckouppgift 2, Övning 4 (version 2) - Temperaturomvandling från Cels->Fahr eller Fahr>Cels
print("Veckouppgift 2, Övning 4 (version 2), Temperaturomvandling Celsius/ Fahrenheit")
temp_choice = (input("Vill du omvandla från Celsius->Fahrenheit, skriv C. Om du vill omvandla från Fahrenheit->Celsius, skriv F: "))
print(f"Du valde att konvertera från {temp_choice}.")
#while True:
#   if temp_choice == "c" or temp_choice == "C" or temp_choice == "f" or temp_choice == "F":
#        break
#    else:
#        print("Du har gjort ett felaktigt val!")
#Fick hjälp av AI att göra en fungerande while sats, den ovan gick in i en evig loop vid felaktigt val
while temp_choice not in ['c', 'C', 'f', 'F']:
    print("Du har gjort ett felaktigt val!")
    temp_choice = input("Vill du omvandla från Celsius->Fahrenheit, skriv C. Om du vill omvandla från Fahrenheit->Celsius, skriv F: ")
if temp_choice in ['c', 'C']:
    #temp_choice == "c" or temp_choice == "C": # Bättre förslag från AI som jag använde i min kod istället
    celsius_degree = float(input("Ange grader i Celcius: "))
    fahr_conv_celc = 1.8 * celsius_degree + 32  # Formel för konvertering från Celsius till Fahrenheit
    print(f"Det blir {fahr_conv_celc} grader Fahrenheit")

elif temp_choice in ['f', 'F']:
    #temp_choice == "f" or temp_choice == "F": # bättre förslag från AI
    fahrenheit_degree = float(input("Ange grader i Fahrenheit: "))
    cels_conf_fahr = (fahrenheit_degree - 32) / 1.8  # Formel för konvertering från Fahrenheit till Celsius
    #print(f"Det blir {cels_conf_fahr} grader Celsius") # Mitt resultat ger för många decimaler
    print(f"Det blir {round(cels_conf_fahr, 1)} grader Celsius") # Jag fick hjälp av av klasskamrat att avrunda till en decimal

