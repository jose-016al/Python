    # CONSTANTES
from posixpath import split
SALIDA = "SALIR"
ARCHIVO_LISTA = "Lista compra.txt"

def pregunta_usuario():
    return input("Introduce un producto [{} para salir]: ".format(SALIDA))

def guardar_lista(lista_compra):
    with open(ARCHIVO_LISTA, "w") as mi_fichero:
        mi_fichero.write("\n".join(lista_compra))

def guardar_item_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto {} ya esta en la lista".format(item_a_guardar))
    else: 
        lista_compra.append(item_a_guardar)

def cargar_o_crear_lista():
    lista_compra = []
    if input("¿Te interesa cargar la ultima lista de la compra? [si/no] ") == "si":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("No existe el fichero")
    return lista_compra

def mostar_lista(lista_compra):
    print("\n".join(lista_compra))

def main():

        # VARIABLES
    lista_compra = cargar_o_crear_lista()
    mostar_lista(lista_compra)

        # main loop
    input_usuario = pregunta_usuario()

    while input_usuario != "SALIR":
        guardar_item_lista(lista_compra, input_usuario)
        input_usuario = pregunta_usuario()

    mostar_lista(lista_compra)
    guardar_lista(lista_compra)

if __name__ == "__main__":
    main()