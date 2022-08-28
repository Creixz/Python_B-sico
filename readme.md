# Curso Básico de Python

## ¿Qué es python?

## Operadores Matemáticos en python

- En python se usan los operadores `+, - , x, /` para las 4 operaciones fundamentales.
- En python si multiplicamos una cadena por un número se repite la cadena sin espacios tantas veces como número se haya indicado.
- Se puede concatenar cadenas de texto con el operador +
- Python no acepta la coma como separador de un decimal.
- En python los valores booleanos son: True y False. (Empieza con mayúscula)

## Conversión

- Se sabe que cuando se ingresa el siguiente código:
 `numero = input("Escribe un numero: ")`
el tipo de variable que se almacena es String, por lo que para convertir a integer se usa:
 `numero = int(numero)`
- Para convertir un entero o float a un string se usa:
    `numero = str(numero)`
- Se puede usar la función `round(variable, nro_decimales)` para redondear la cantidad de decimales que tendrá el float.

## Operadores Lógicos

- Para utilizar el "y" se utiliza en python `and`
- Para utilizar el "o" se coloca en python `or`
- Para negar el valor booleano de una variable se utiliza en python `not`
- Para comparar, es decir, saber si el contenido de dos variables es el mismo, se usar `==` que te devuelve un booleano.
- Para comparar de forma negativa, es decir si el contenido de dos variables es diferente se usa `!=` y devuelve un booleano.
- Para comparaciones de mayor, menor y/o igual se usar `< >` y de igual manera te devuelve un booleano. 

## Condicionales

- Para utilizar condiciones se sigue la siguiente estructura:
`if numero > 5:` no se utiliza paréntesis y al colocar la condición debe dejarse 4 espacios.
- Se puede usar `elif numero == 5:` si es que hay más condiciones que se pueden evaluar.
- Se pueden colocar como condición `pass` si es que no se tiene alguna condición específica o se decia dejar asi por el momento.

## Funciones de Python

- Son piezas de código reutilizables que reciben arguementos como input para realizar algunos cálculos y luego devolver uno o más resultados.
- Existen dos tipos de funciones:
    1. Funciones incorporadas: Son aquellas que son parte de Python como `print()`, `type()`, `float()`, etc.
    2. Funciones que nosotros definimos: Tratamos a los nombres de las funciones como "nuevas" palabras reservadas, es decir, ya no
    se pueden usar como variables.
- Para definir una variable se usa la palabra reservada `def`.
- Una vez que la hemos definido podremos llamarla o invocarla todas las veces que querramos.
- Cuando se define una función **recordar** que eso no ejecuta la función:  
```
    def print_lyrics():  
        print("Todo estará bien.")
```
-
- Un parámetro es una variable que utilizamos en la definición de la función y esto permite al código de la función acceder a los argumentos para realizar cálculos.  
```
    def print_lyrics(**argumento**):  
        print("Todo estará bienx2.")
```

## Trabajando con texto

- Python puede entender y respetar tus string respetando las lineas que haz utilizado si utilizas la triple comilla doble. (varias lineas de caracteres)
- Utilizando el método `nombre.upper()` para colocar todo el texto en mayúsculas.
- Utilizando el método `nombre.capitalize()` para solo colocar el mayúscula la primera letra del texto.
- Utilizando el método `nombre.strip()` elimina los espacios entre texto.
- utilizando el método `nombre.lower()` para colocar todo el texto en minúscula.
- Utilizando el método `nombre.replace('letra_a_reemplazar','letra_que_reemplaza')` reemplaza una letra por otra en todo el texto.
- Puedo obtener cualquier caracter de un texto con los índices `nombre[n]` donde n empieza en 0.
- Puedo determinar la longitud o la cantidad de caracteres que tiene mi texto, se usa la función `len(nombre)`.


