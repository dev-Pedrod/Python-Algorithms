import random

elementos = random.sample(range(10), 10)
print(sorted(elementos))


def busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False


valor_retorno = busca_linear(elementos, 11)
print(valor_retorno)

## função index()
vogais = 'aeiou'
resultado = vogais.index('u')
print(resultado)


# Será que conseguimos implementar a nossa própria versão de busca por index com utilização da busca linear?
# A resposta é sim! Podemos iterar sobre a lista e, quando o elemento for encontrado, retornar o seu índice.
# Caso não seja encontrado, então a função deve retornar None.

def procurar_valor(lista, valor):
    for i in range(len(lista)):
        if valor == lista[i]:
            return i
    return None


def testar_resultado(resultado):
    if resultado:
        print(f"Valor encontrado na posição {resultado}")
    else:
        print("Valor não encontrado")


vogais = ['a', 'e', 'i', 'o', 'u']

# Usando nossa função
resultado = procurar_valor(vogais, 'e')
testar_resultado(resultado)
