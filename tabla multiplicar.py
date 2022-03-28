# introducimos un numero y mostramos la tabla de multiplicar de dicho numero 
numero = int(input("Numero a multiplicar: "))

for item in range(1, 11):
    # if item % 2 == 0:
    print("{} x {} = {}".format(item, numero, item * numero))