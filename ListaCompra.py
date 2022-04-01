    # CONSTANTES
SALIDA = "SALIR"
LISTA = "LISTA"

def pregunta_usuario():
    return input("Introduce un producto [{} para salir]: ".format(SALIDA))

def guardar_lista(lista_compra):
    nombre = input("Como quieres llamar el archivo: ")
    with open(nombre + ".txt", "w") as mi_fichero:
        mi_fichero.write("\n".join(lista_compra))

def guardar_item_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto {} ya esta en la lista".format(item_a_guardar))
    else: 
        lista_compra.append(item_a_guardar)

def main():

        # VARIABLES
    lista_compra = []

        # main loop
    input_usuario = pregunta_usuario()

    while input_usuario != "SALIR":
        guardar_item_lista(lista_compra, input_usuario)
        print("\n".join(lista_compra))
        input_usuario = pregunta_usuario()

    guardar_lista(lista_compra)

if __name__ == "__main__":
    main()