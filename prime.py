# Primzahlen überprüfen

zahl = input("Geben sie eine Zahl ein ")
z = int(zahl)
isPrime = False

for i in range(2,z):
    if(z % i == 0):
        isPrime = True

if(isPrime):
    print(z,"ist keine Primzahl",sep=" ")
else:
    print(z,"ist eine Primzahl",sep=" ")

