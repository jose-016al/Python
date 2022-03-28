lista_numeros = []
numero = 0

while numero != -1:
    numero = int(input("Introduce un numero (-1 termina el proceso): "))
    lista_numeros.append(numero)

mayor = lista_numeros[0]
menor = lista_numeros[0]

for numero in lista_numeros[1:]:
    if mayor < numero:
        mayor = numero
    elif menor > numero:
        menor = numero
    
print("El numero mayor de la lista es: {}".format(mayor))
print("El numero menor de la lista es: {}".format(menor))