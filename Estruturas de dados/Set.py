#A tradução"conjunto" para set  nos leva diretamente à essência desse tipo de estrutura de dados em Python.
# Um objeto do tipo set habilita operações matemáticas de conjuntos, tais como: união, intersecção, diferenteça, etc.
# Esse tipo de estrutura pode ser usado, portanto, em testes de associação e remoção de valores duplicados de uma sequência
# (PSF, 2020c).

# Das operações que já conhecemos sobre sequências, conseguimos usar nessa nova estrutura:
# len(s)
# x in s
# x not in s
# Além dessas operações, podemos adicionar um novo elemento a um conjunto com a função add(valor).
# Também podemos remover com remove(valor). Veja uma lista completa de funções no endereço https://bit.ly/2NF7eIT.

# Em Python, os objetos do tipo set podem ser construídos destas maneiras:
# Usando um par de chaves e elementos separados por vírgulas: set1 = {'a', 'b', 'c'}
# Usando o construtor de tipo: set(iterable)
# Não é possível criar um set vazio, com set = {}, pois essa é a forma de construção de um dicionário.
# Para construir com utilização da função set(iterable), obrigatoriamente temos de passar um objeto iterável para ser
# transformado em conjunto. Esse objeto pode ser uma lista, uma tupla ou até mesmo uma string (que é um tipo de sequência).
# Veja os exemplos de construção a seguir.

vogais_1 = {'aeiou'} # sem uso do construtor
print(type(vogais_1), vogais_1)

vogais_2 = set('aeiouaaaaaa') # construtor com string
print(type(vogais_2), vogais_2)

vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
print(type(vogais_3), vogais_3)

vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
print(type(vogais_4), vogais_4)

print(set('banana'))

# O poder do objeto set está em suas operações matemáticas de conjuntos.
# Vejamos um exemplo: uma loja de informática recebeu componentes usados de um computador para avaliar se estão com defeito.
# As peças que não estiverem com defeito podem ser colocadas à venda.
# Como, então, podemos criar uma solução em Python para resolver esse problema? A resposta é simples:
# usando objetos do tipo set. Observe o código a seguir.

def create_report():
    componentes_verificados = set(
        ['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub',
         'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break',
         'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])

    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)

    componentes_ok = componentes_verificados.difference(componentes_com_defeito)

    print(f"Foram verificados {qtde_componentes_verificados} componentes.\n")
    print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito.\n")

    print("Os componentes que podem ser vendidos são:")
    for item in componentes_ok:
        print(item)


create_report()