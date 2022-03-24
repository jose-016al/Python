# Aprendiendo Python

#### print() muestra la salida del texto y variables que contiene
```python
variable = "Aprendiendo Python"
print(variable)
```
Aprendiendo Python

---

#### .format() da formato a la salida print()
```python
a = "Aprendiendo Python"
print("La variable a contiene: '{}'".format(a))
```
La variable a contiene: 'Aprendiendo Python'

---

#### input() es un medio de entrada para que el usuario introduzca datos, los valores introducidos por input() son de tipo String para que sean numeros tenemos que poner el tipo antes del input()
```python
a = input("Introduce un valor para la variable: ")
print("La variable 'a' contiene: '{}'".format(a))
numero = int(input("Introduce un numero: "))
print("La vriable 'numero' contiene: '{}'".format(numero))
```
Introduce un valor para la variable: Aprendiendo python
La variable 'a' contiene: 'Aprendiendo python'
Introduce un numero: 50
La vriable 'numero' contiene: '50'

---

#### Con la funcion random obtenemos numeros aleatorios 
```python
import random 
aleatorio = random.randint(1, 10)
print("El numero aleatorio generado ha sido: {}".format(aleatorio))
```
El numero aleatorio generado ha sido: 10

---

#### if y else 
```python
if numero > 1 and numero < 10:
    if numero == aleatorio:
        print("Enhorabuena has ganado")
    else :
        print("Vaya... Has perdido, el numero correcto era: {}".format(aleatorio))
else :
    print("ERROR, el numero tiene que estar entre 1 y 10")
```
Vaya... Has perdido, el numero correcto era: 7

---

#### len() nos muestra el tamaño de la variable que pasamos por parametro
```python
a = "Aprendiendo python"
print("El tamaño de la variable 'a' es: {}".format(len(a)))
```
El tamaño de la variable 'a' es: 18

---

#### Usando len() para crear una subrayado automatico
```python
titulo = "Aprendiendo python"
print(titulo + "\n" + "-" * len(titulo) + "\n")
```
Aprendiendo python
------------------

---

#### Se pueden hacer menus con input()
```python
opcion = input("Introduce una opcion \n"
                "A - convertir de dolar a euro \n"
                "B - convertir de euro a dolar \n"
                "C - convertir de libra a euro \n"
                "D - convertir de euro a libra \n")
```
Introduce una opcion 
A - convertir de dolar a euro 
B - convertir de euro a dolar 
C - convertir de libra a euro 
D - convertir de euro a libra 

---