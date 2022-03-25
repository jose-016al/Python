opcion = None
while opcion != "A" and opcion != "B" and opcion != "C":
    opcion = input("Introduce una opcion ")
    if opcion != "A" and opcion != "B" and opcion != "C":
        print("Opcion incorrecta")

if opcion == "A":
    print("Has escogido la opcion A")
elif opcion == "B":
    print("Has escogido la opcion B")
else:
    print("Has escogido la opcion C")