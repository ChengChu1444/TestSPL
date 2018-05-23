# Primzahlen überprüfen

# Effizienter als die letzte Methode

def zerlegPrime(wert):
    w = int(wert)
    counter = 2
    done = False
    while(counter <= w and done == False):
        isPrimeF = False
        for i in range(2,counter):
             if(counter % i == 0):
                isPrimeF = True

        if(isPrimeF == False):
            if(w % counter == 0):
                print(counter)
                zerlegPrime(w/counter)
                done = True
        counter=counter+1

zahl = input("Geben sie eine Zahl ein ")
z = int(zahl)
zerlegPrime(z)
