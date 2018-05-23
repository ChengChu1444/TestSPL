# Primzahlen überprüfen

# Sehr ineffizient, aber funktionstüchtig

def zerlegPrime(wert):
    w = int(wert)
    counter = w-1
    done = False
    while(counter > 1 and done == False):
        isPrimeF = False
        for i in range(2,counter):
             if(counter % i == 0):
                isPrimeF = True

        if(isPrimeF == False):
            if(w % counter == 0):
                print(counter)
                zerlegPrime(w/counter)
                done = True
        counter=counter-1
    if(w-1==1):
      print(w)

zahl = input("Geben sie eine Zahl ein ")
z = int(zahl)
zerlegPrime(z)
