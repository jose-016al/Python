titulo = "Programa lista de la compra"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

lista = []
opcion = None
while opcion != "Q":
    opcion = input("Que desea comprar (Q salir del programa): ")
    if opcion in lista:
        print("{} ya esta en la lista \n".format(opcion))
    else:
        if input("Estas seguro de que quieres añadir {} (s/n): ".format(opcion)) == "s":
            lista.append(opcion)
            print("\n")

print("\n La lista de la compra es:")
print(lista)