# Juego para adivinar un numero 
import random
aleatorio = random.randint(1, 10)
numero = int(input("Introduce un numero entre 1 y 10: "))

if numero > 1 and numero < 10:
    if numero == aleatorio:
        print("Enhorabuena has ganado")
    else :
        print("Vaya... Has perdido, el numero correcto era: {}".format(aleatorio))
else :
    print("ERROR, el numero tiene que estar entre 1 y 10")