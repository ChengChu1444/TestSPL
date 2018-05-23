from array import array
# Primzahlen überprüfen

def zerlegPrime(wert):
    w = int(wert)
    counter = w-1
    
    while(counter > 1):
        isPrimeF = False
        for i in range(2,counter):
             if(counter % i == 0):
                isPrimeF = True
        if(isPrimeF == False):
            if(w % counter == 0):
                print(counter)
                zerlegPrime(w/counter)
        counter=counter-1

zahl = input("Geben sie eine Zahl ein ")
z = int(zahl)
zerlegPrime(z)




