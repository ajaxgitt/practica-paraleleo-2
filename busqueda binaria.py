def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio  # Retorna el índice donde se encontró el objetivo
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # Retorna -1 si el objetivo no está en la lista


# Ejemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13]
indice = busqueda_binaria(numeros, 7)
print("Índice encontrado:", indice)  # Salida: Índice encontrado: 3
