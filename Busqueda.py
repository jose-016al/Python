# El usuario introuduce una frase y se cuenta los espacios, puntos y comas
espacios = 0
puntos = 0
comas = 0

frase = input("Introduce una frase: ")

for letra in frase:
    if letra in " ":
        espacios += 1
    elif letra in ".":
        puntos += 1
    elif letra in ",":
        comas += 1

print("espacios {}".format(espacios))
print("puntos {}".format(puntos))
print("comas {}".format(comas))