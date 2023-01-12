import numpy as np

# crear lista con numeros primos

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# crear array a partir de lista 

array_primos = np.array(numeros_primos)

print(array_primos)

# crear arrays con ceros o como inicializar un arreglo de numpy

array_zeros = np.zeros(10)

print(array_zeros)

# crear arrays con numeros

array_numeros = np.arange(10)
print(array_numeros)

# array con numeros sucesivos
array_pares = np.arange(0, 20, 2)
print(array_pares)

#haciendo un reshape para dos dimensiones
reshape_dosdimensiones = array_pares.reshape(2,5)
print(reshape_dosdimensiones)

#operaciones aritmeticas sobre np array 1-dimension y 2-dimension
array_impares = array_pares + 1
print(array_impares)

# multiplicar por 100
multiplicado_por_100 = array_impares * 100
print(multiplicado_por_100)

# resta entre arrays
resta_array = array_impares - array_pares
print(resta_array)

# cuidado con la division entre cero (inf)
division_array = array_impares / array_pares
print(division_array)

# metodos asociados a estadistica
# suma
suma_array = array_primos.sum()
print(suma_array)

# promedio
promedio_array = array_primos.mean()
print(promedio_array)

#varianza
varianza_array = array_primos.var()
print(varianza_array)

# como ordenar un np array
array_fibonacci = np.array([55, 0, 144, 1, 21, 89, 5, 8, 13, 1, 34, 2])
print(array_fibonacci)

# orden ascendente: de menor a mayor
array_ascendente = np.sort(array_fibonacci)
print(array_ascendente)

# orden descendente: de mayor a menor
array_descendente =- np.sort(-array_ascendente)
print(array_descendente)

# Como seleccionar elements
# Seleccionar un elemento
A = np.arange(0,20,2).reshape(2,5)
print(A)

# seleccionar el primer elemento
primer_elemento = A[0,0]
print(primer_elemento)

# seleccionar algun otro elemento
seleccionar_otro = A[1,4]
print(seleccionar_otro)

# Seleccionar varios elementos
# seleccionar por fila 
seleccionar_fila = A[1, :]
print(seleccionar_fila)

# seleccionar por columna
seleccionar_columna = A[:,3]
print(seleccionar_columna)

# Utilizar filter
# condicion para menores de 20, booleana
menores_20 = array_fibonacci < 20
print(menores_20)

# filtrar menores de 20
filtrado_menores_20 = array_fibonacci[array_fibonacci< 20]
print(filtrado_menores_20)