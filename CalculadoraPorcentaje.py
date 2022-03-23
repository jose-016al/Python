print("---------------------CALCULADORA DE PORCENTAJES-------------------- \n")
repetir = True
while repetir == True:
    dinero = float (input("Introduce el dinero: "))
    if dinero > 0:
        porcentaje = int(input("Introduce el porcentaje: "))
        resultado = (porcentaje * dinero) / 100
        print("El", porcentaje, "% de", dinero, "€ es", resultado, "\n")
    else:
        repetir = False
print("------------------------PROGRAMA FINZALIZADO-----------------------")