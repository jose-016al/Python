# El usuario introuduce una frase y se cuentan las mayusculas
import string
mayusculas = 0

frase = input("Introduce una frase: ")

for letra in frase:
    if letra in string.ascii_uppercase:
        mayusculas += 1

print("Mayusculas {}".format(mayusculas))
