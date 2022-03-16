# As tuplas também são estruturas de dados do grupo de objetos do tipo sequência.
# A grande diferença entre listas e tuplas é que as primeiras são mutáveis
# razão pela qual, com elas, conseguimos fazer atribuições a posições específicas:
# por exemplo, lista[2] = 'maça'. Por sua vez, nas tuplas isso não é possível uma vez que são objetos imutáveis.

# Em Python, as tuplas podem ser construídas de três maneiras:
# Usando um par de parênteses para denotar uma tupla vazia: tupla1 = ()
# Usando um par de parênteses e elementos separados por vírgulas: tupla2 = ('a', 'b', 'c')
# Usando o construtor de tipo: tuple()

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

for item in enumerate(vogais):
    print(item)