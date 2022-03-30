def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo - 1)
        executar_quicksort(lista, pivo + 1, fim)
    return lista


def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    return esquerda


lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_quicksort(lista, inicio=0, fim=len(lista) - 1))


def executar_quicksort_2(lista):
    if len(lista) <= 1: return lista
    pivo = lista[0]
    iguais = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor < pivo]
    maiores = [valor for valor in lista if valor > pivo]
    return executar_quicksort_2(menores) + iguais + executar_quicksort_2(maiores)


lista = [10, 9, 5, 8, 11, -1, 3]
print(executar_quicksort_2(lista))
