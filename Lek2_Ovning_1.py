#https://github.com/Anette1974/Lesson2_Conditions.git
print("Veckouppgift 2, Övning 1")
is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)
#if price > level1: # Man får inte rabatt för köp på 100 kr utan från 101 kr. Man får även rabatten för level 1 och 2 vid köp över 300
if price >= level1 and price < level2: # här behövdes <= och ett villkor för under 300
    print ("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
#if price >= level2:
elif price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
#print("Efter rabatter blir priset..." + final_price) # Saknas en konvertering från float till str
print("Efter rabatter blir priset..." + str(final_price))
