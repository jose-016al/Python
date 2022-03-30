# Aprendiendo Python

## La funcion print() para la salida de datos

#### print() muestra la salida del texto y variables que contiene
```python
variable = "Aprendiendo Python"
print(variable)
```
> Aprendiendo Python

#### Por defecto la funcion print() nos hace un salto de linea, si queremos evitar esto usamos end="" con esto estamos indicando que siga en la misma linea el siguiente print()
```python
print("Aprendiendo ", end="")
print("Python")
```
> Aprendiendo Python

#### .format() da formato a la salida print()
```python
a = "Aprendiendo Python"
print("La variable a contiene: '{}'".format(a))
```
> La variable a contiene: 'Aprendiendo Python'

## La funcion input() para la entrada de datos

#### input() es un medio de entrada para que el usuario introduzca datos, los valores introducidos por input() son de tipo String para que sean numeros tenemos que poner el tipo antes del input()
```python
a = input("Introduce un valor para la variable: ")
print("La variable 'a' contiene: '{}'".format(a))
numero = int(input("Introduce un numero: "))
print("La vriable 'numero' contiene: '{}'".format(numero))
```
> Introduce un valor para la variable: Aprendiendo python  
La variable 'a' contiene: 'Aprendiendo python'  
Introduce un numero: 50  
La vriable 'numero' contiene: '50' 

## Como hacer un menu en python

#### Se pueden hacer menus con input()
```python
opcion = input("Introduce una opcion \n"
                "A - convertir de dolar a euro \n"
                "B - convertir de euro a dolar \n"
                "C - convertir de libra a euro \n"
                "D - convertir de euro a libra \n")
```
> Introduce una opcion  
A - convertir de dolar a euro  
B - convertir de euro a dolar  
C - convertir de libra a euro  
D - convertir de euro a libra  

## Los condicionales: if, elif y else

#### if y else 
```python
if numero > 1 and numero < 10:
    if numero == aleatorio:
        print("Enhorabuena has ganado")
    else:
        print("Vaya... Has perdido, el numero correcto era: {}".format(aleatorio))
else:
    print("ERROR, el numero tiene que estar entre 1 y 10")
```
> Vaya... Has perdido, el numero correcto era: 7

## El bucle while

#### En buble while siempre se debe incializar una variable a None
```python
opcion = None
while opcion != "A" and opcion != "B" and opcion != "C":
    opcion = input("Introduce una opcion ")
    if opcion != "A" and opcion != "B" and opcion != "C":
        print("Opcion incorrecta")
```
> Introduce una opcion hola  
Opcion incorrecta  
Introduce una opcion C  
Has escogido la opcion C  

## Las listas

#### Las listas se incializan con [], con .append() añadimos objetos a la lista, con .pop() eliminamos objetos de la lista y con in buscamos un objeto en la lista
```python
lista = []
lista.append(1)
lista.append(2)
print(lista)
if 50 in lista:
    print("Esta en la lista")
else:
    print("No esta en la lista")
lista.pop(1)
print(lista)
```
> [1, 2]  
No esta en la lista  
[1]  

## El bucle for 

#### El bucle for recorriendo una lista 
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in a:
    print(item)
```
> 1 2 3 4 5 6 7 8 9 10

#### El bucle for se puede recorrer con un rango 
```python
for item in range(1, 11):
    print("{} x {} = {}".format(item, numero, item * numero))
```
> 1 x 5 = 5  
2 x 5 = 10    
3 x 5 = 15  
4 x 5 = 20  
5 x 5 = 25  
6 x 5 = 30  
7 x 5 = 35  
8 x 5 = 40  
9 x 5 = 45  
10 x 5 = 50

#### Podemos filtrar el bucle for con [], es decir con [1:] estariamos filtrando el for para que se salte la posicion 0 y empice por la 1 o podemos poner [1:5] el for recorrera la lista dese la posicion 0 hasta la 4
```python
lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista_numeros[1:5]:
    print(numero)
```
> 1  
2  
3  
4  

## Algunas funciones de python

#### Con la funcion random obtenemos numeros aleatorios 
```python
import random 
aleatorio = random.randint(1, 10)
print("El numero aleatorio generado ha sido: {}".format(aleatorio))
```
> El numero aleatorio generado ha sido: 10

#### len() nos muestra el tamaño de la variable que pasamos por parametro
```python
a = "Aprendiendo python"
print("El tamaño de la variable 'a' es: {}".format(len(a)))
```
> El tamaño de la variable 'a' es: 18

#### Usando len() para crear una subrayado automatico
```python
titulo = "Aprendiendo python"
print(titulo + "\n" + "-" * len(titulo) + "\n")
```
> Aprendiendo python  
> ------------------

#### Con la funcion os.system(clear) limpiamos la pantalla, en windows usamos os.system(cls)
```python
import os 
contador = 0
while contador != 5:
    print("Aprendiendo python")
    if contador > 0 and contador < 5:
        contador+=1
    else:
        os.system("clear")
```
Nos muestra solo una linea en vez de 5 ya que la pantalla se va borrando  
> Aprendiendo python 