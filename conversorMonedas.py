# introducimos una cantidad y la convierte a la moneda que seleccionamos
dolar_euro = 0.91
libra_euro = 1.18

opcion = input("Introduce una opcion \n"
                "A - convertir de dolar a euro \n"
                "B - convertir de euro a dolar \n"
                "C - convertir de libra a euro \n"
                "D - convertir de euro a libra \n")

texto_usuario = "Introduce la cantidad de {} a convertir: "

if opcion == "A":
    cantidad_dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad de euros es: {}".format(cantidad_dinero * dolar_euro))
elif opcion == "B":
    cantidad_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad de dolares es: {}".format(cantidad_dinero / dolar_euro))
elif opcion == "C":
    cantidad_dinero = float(input(texto_usuario.format("libras")))
    print("La cantidad de euros es: {}".format(cantidad_dinero * libra_euro))
elif opcion == "D":
    cantidad_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad de libras es: {}".format(cantidad_dinero / libra_euro))
else:
    print("Opcion incorrecta")