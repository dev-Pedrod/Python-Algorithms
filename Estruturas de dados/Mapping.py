# As estruturas de dados que possuem um mapeamento entre uma chave e um valor são consideradas objetos do tipo mapping.
# Em Python, o objeto que possui essa propriedade é o dict (dicionário).
# Uma vez que esse objeto é mutável,  conseguimos atribuir um novo valor a uma chave já existente.

# Podemos construir dicionários em Python das seguintes maneiras:
# Usando um par de chaves para denotar um dict vazio: dicionario1 = {}
# Usando um par de elementos na forma, chave : valor separados por vírgulas: dicionario2 = {'one': 1, 'two': 2, 'three': 3}
# Usando o construtor de tipo: dict()
# Observe os exemplos a seguir com maneiras de construir o dicionário.

# Exemplo 1 - Criação de dicionário vazio, com atribuição posterior de chave e valor
dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 30

# Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
dici_2 = {'nome': 'João', 'idade': 30}

# Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
dici_3 = dict([('nome', "João"), ('idade', 30)])

# Exemplo 4 - Criação de dicionário com a função built-in zip() e duas listas, uma com as chaves, outra com os valores.
dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))


print(dici_1 == dici_2 == dici_3 == dici_4) # Testando se as diferentes construções resultamo em objetos iguais.

# Uma única chave em um dicionário pode estar associada a vários valores por meio de uma lista, tupla ou até mesmo outro dicionário.
# Nesse caso, também conseguimos acessar os elementos internos. No código a seguir, a função keys() retorna uma lista
# com todas as chaves de um dicionário. A função values() retorna uma lista com todos os valores.
# A função items() retorna uma lista de tuplas, cada uma das quais é um par chave-valor.

cadastro = {
            'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
            'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
            'idade' : [25, 33, 37, 18]
            }

print("len(cadastro) = ", len(cadastro))

print("\n cadastro.keys() = \n", cadastro.keys())
print("\n cadastro.values() = \n", cadastro.values())
print("\n cadastro.items() = \n", cadastro.items())

print("\n cadastro['nome'] = ", cadastro['nome'])
print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])

print(len(cadastro['nome']))
print(len(cadastro['cidade']))
print(len(cadastro['idade']))

qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])

print(f"\n\nQuantidade de elementos no dicionário = {qtde_itens}")