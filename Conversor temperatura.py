# introducimos un valor de grados fahrenheit y lo comvertimos a grados celsius
grados_fahrenheit = int(input("¿ Grado Fahrenheit ? "))
grados_celsius = (grados_fahrenheit - 32) * 5 / 9

print("El resultado es: {}".format(grados_celsius))