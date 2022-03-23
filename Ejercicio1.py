# Introducimos tres valores y nos indica cual es el mayor y el menor
numero1 = int(input("Introduce el primer numero "))
numero2 = int(input("Introduce el segundo numero "))
numero3 = int(input("Introduce el tercero numero "))

print("El numero mas grande entre {}, {} y {} es: {} y el mas pequeño es: {}".format(numero1, numero2, numero3,
max(numero1 ,numero2, numero3),
min(numero1, numero2, numero3)))
