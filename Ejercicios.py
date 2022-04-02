import random


#Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más  larga de todas
def string_mas_larga(lista):
    max = len(lista[0])
    mas_larga = lista[0]
    for n in lista:
        if len(n) > max:
            mas_larga = n
    return mas_larga

# Crea una función que sume una lista de números, no se vale usar la función sum()
def suma(lista):
    resultado = 0
    for n in lista:
        resultado += n
    return resultado

# Crea una función que te de True como resultado si el número pasado como argumento es impar
def es_impar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False

# Crea una función que pregunte al usuario si esta seguro o no, y devuelva los valores "True" o "False" dependiendo de si el usuario está seguro.
def seguro():
    string = input("Estas seguro [si/no]: ")
    while string.lower() != "si" and string.lower() != "no":
        print("{} no es una opcion disponible ".format(string.lower()))
        string = input("Estas seguro [si/no]: ")
    if string.lower() == "si":
        return True
    elif string.lower() == "no":
        return False

# Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()
def mayus(string):
    return string.upper()

'''
Crea una función que reciba como argumento un número del 1 al 100 a adivinar y 
que le pregunte al usuario que adivine el número. El código se ejecutará hasta que 
el usuario adivine.
'''
def adivina():
    aleatorio = random.randint(1, 100)
    numero = 0
    while numero != aleatorio:
        numero = int(input("Introduce un numero [entre 1 y 100]: "))
        if numero == aleatorio:
            return "Muy bien haz acertado"
        else:
            print("Vas muy mal en caminado, prueba con {}".format(aleatorio))

def main():
    lista_string = ["hola", "como", "estas"]
    print(string_mas_larga(lista_string))

    lista_numeros = [450, 80, 1200]
    print(suma(lista_numeros))

    print(es_impar(3))
    print(es_impar(24))

    print(seguro())

    print(mayus("aprendiendo python"))

    print(adivina())

if __name__ == "__main__":
    main()
