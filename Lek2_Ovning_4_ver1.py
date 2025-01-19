# Veckouppgift 2, Övning 4 (version 1) - Temperaturomvandling endast från Cels->Fahr
print("Veckouppgift 2, Övning 4 (version 1), Temperaturomvandling endast från Celsius till Fahrenheit")
celcius_degree = float(input("Vad är temperaturen i Celsius som du vill omvandla till Fahrenheit? "))
fahrenheit_converted = 1.8 * celcius_degree + 32 # Formel för konvertering från Celsius till Fahrenheit
print (f"Det blir {fahrenheit_converted} grader Fahrenheit")