# Veckouppgift 2, Övning 2
'''För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!

Fråga användaren hur lång man är (i cm)
Skriv ut antingen "Du får åka!" eller "Du får inte åka"

Skriv in följande värden för att testa att ditt program gjort rätt:
121 cm (får inte åka)
130 cm (får åka)
155 cm (får åka)

Diskutera:
Varför just tre värden?
Varför dessa värden?
Skulle det vara bra att lägga till testvärdet 129 cm?'''

print("Veckouppgift 2, Övning 2")
length = int(input("Ange din längd i cm: "))
if length >= 130:
    print (f"Grattis, du får åka Balder när du är {length} cm lång")
else:
    print(f"Du är tyvärr för kort för att åka Balder när du endast är {length} cm lång")