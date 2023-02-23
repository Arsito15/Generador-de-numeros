import random

def generar_numeros(cantidad, archivo):
    with open(archivo, 'w') as file:
        for i in range(cantidad):
            num = random.randint(-10000000, 10000000)
            file.write(str(num) + '\n')

def ordenar_numeros(archivo_origen, archivo_destino):
    numeros = {}
    with open(archivo_origen, 'r') as origen:
        for linea in origen.readlines():
            num = int(linea.strip())
            if num not in numeros:
                numeros[num] = 1
    with open(archivo_destino, 'w') as destino:
        for num in sorted(numeros.keys()):
            destino.write(str(num) + '\n')

    # Algoritmo de ordenamiento de burbuja
    n = len(numeros)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numeros[j] > numeros[j+1] :
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    with open(archivo_destino, 'w') as destino:
        for num in numeros:
            destino.write(str(num) + '\n')

while True:
    opcion = input('¿Qué deseas hacer?\n1. Generar números aleatorios\n2. Ordenar números\n3. Salir\n')
    if opcion == '1':
        cantidad = int(input('¿Cuántos números quieres generar?\n'))
        archivo = input('Ingresa el nombre del archivo donde se guardarán los números:\n')
        generar_numeros(cantidad, archivo)
        print('Números generados correctamente')
    elif opcion == '2':
        archivo_origen = input('Ingresa el nombre del archivo que contiene los números sin ordenar:\n')
        archivo_destino = input('Ingresa el nombre del archivo donde se guardarán los números ordenados:\n')
        ordenar_numeros(archivo_origen, archivo_destino)
        print('Números ordenados correctamente')
    elif opcion == '3':
        print('Saliendo del programa...')
        break
    else:
        print('Opción no válida')