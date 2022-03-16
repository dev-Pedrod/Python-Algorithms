vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')


# Mesmo resultado.
vogais = []
print(f"\nTipo do objeto vogais = {type(vogais)}\n")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")


frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas) # True
print("abacate" in frutas) # False
print("abacate" not in frutas) # True
print(min(frutas)) # banana
print(max(notas)) # 10
print(frutas.count("maça")) # 2
print(frutas + notas)
print(2 * frutas)


lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]
print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")

print("Exemplos de slices:")

print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])


# LIST COMPREHENSION

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() Essa sintaxe produz o mesmo resultado que a linha 1

print("\nAntes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("Depois da listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = [item for item in linguagens if "Java" in item]

print("\n",linguagens_java)

# FUNÇÕES MAP() E FILTER()

# Exemplo 1
print("Exemplo 1")
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")


# Exemplo 2
print("\n\nExemplo 2")
numeros = [0, 1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x*x, numeros))
print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")


numeros  = list(range(0, 21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)