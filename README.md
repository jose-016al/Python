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
Tambien se puede crear un for en una sola linea
```python
if item_a_guardar in [a for a in lista_compra]:
    print("El producto {} ya esta en la lista".format(item_a_guardar))
else: 
    lista_compra.append(item_a_guardar)

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

#### Podemos convertir a minusculas '.lower()' o mayusculas '.upper()'
```python
if item_a_guardar.lower() in [a.lower() for a in lista_compra]:  
    print("El producto {} ya esta en la lista".format(item_a_guardar))  
else:   
    lista_compra.append(item_a_guardar)  
```

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

#### Con os.getlogin() nos muestra el usuario del sistema
```python
import os

def main():
    open("LEEME.txt", "a")
    print(os.getlogin())

if __name__ == "__main__":
    main()
```
> jose

#### El funcionamiento de sleep() para esperar un tiempo antes de hacer algo
```python
from time import sleep
from random import randrange

def main():

    numero_horas = randrange(1, 4)
    numero_minutos = randrange(0, 60)
    print("Durmiendo {} horas, {} minutos".format(numero_horas, numero_minutos))
    sleep(numero_horas * 60 * 60)
    sleep(numero_minutos * 60)
```
> Durmiendo 1 horas, 14 minutos  

## Nuestras propias funciones

#### Con def creamos nuestra funcion y podemos pasar parametros en los parentesis
```python
def saludar(nombre):
    print("Hola {}".format(nombre))

saludar("Jose")
```
> Hola Jose  

#### Podemos pedirle a la funcion que nos devuelva un valor
```python
def largo_frase(frase):
    largo = 0
    for i in frase:
        largo += 1
    return largo

num_letras = largo_frase("Aprendiendo python")
print("El numero de letras en la frase es: {}".format(num_letras))
```
> El numero de letras en la frase es: 18  

## La programacion funcional

#### La programacion funcional consiste en dividir nuestro codigo en diversos metodos o fucniones, y una vez terminado en una funcion main() volcarlo todo, y por ultimo haremos una condicion 
'if __name__ == "__main__"'
```python
def suma(n1, n2):
    resultado = n1 + n2
    return resultado

def main():
    print(suma(2, 2))

if __name__ == "__main__":
    main()
```
> 4  

## Trabajando con ficheros 

#### Con open() abrimos un ficero indicamos el nombre y el modo en el que se abre, 'w' es escritura crea el archivo si no existe o lo reescribe, con 'a' se van añadiendo lo que queramos, 'r' es lectura, usamos write() para escribir en el fichero. Hay dos formas de hacer esto
```python
a = open("fichero.txt", "w")
a.write("\n".join(lista_compra))
a.close
```
```python
with open("fichero.txt", "w") as mi_fichero:
    mi_fichero.write("\n".join(lista_compra))
```
> Se crea el fichero con lo que le pasemos con .write  

#### Para leer ficheros pasamos por parametro en el open() r para indicar que lo abra en modo lectura
```python
lista_compra = []

if input("¿Te interesa cargar la ultima lista de la compra? [si/no] ") == "si":
    with open("Lista compra.txt", "r") as a:
        lista_compra = a.read().split("\n")
```
> En este caso metemos cada palabra en una posicion de la lista  

#### Para crear un fichero en una ruta determinada
```python
import os

def main():
    desktop = "/home/" + os.getlogin() + "/"
    with open(desktop + "LEEME.txt", "w") as mi_fichero:
        mi_fichero.write("Soy un haxcker")

if __name__ == "__main__":
    main()
```
> Se crea el fichero

## Gestionando excepciones en python

#### Con try ponemos el codigo a ejecutar y con except ponemos la escepcion que se lanzaria y un mensaje en caso de que se cumpla
```python
lista_compra = []

if input("¿Te interesa cargar la ultima lista de la compra? [si/no] ") == "si":
    try:
        with open(ARCHIVO_LISTA, "r") as a:
            lista_compra = a.read().split("\n")
    except FileNotFoundError:
        print("No existe el fichero")
```
> No existe el fichero

## Las interfaces graficas en python

#### Instalamos PySimpleGui y con el atributo .Window creamos una ventana con un titulo un lista dentro de otra lista y un tamaño, con read() lo lanzamos
```python
import PySimpleGUI as sg

window = sg.Window("Titulo", [[]], margins=(100, 100)).read()
```
> 