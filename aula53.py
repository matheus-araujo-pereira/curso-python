# enumerate - enumera iteráveis (índices)

nomes = ["Matheus", "Tahinae", "Ari"]
nomes.append("Luna")
nomes_enumarados = enumerate(nomes)

for nome in nomes_enumarados:
    print(nome)

lista_nomes_enumarados = list(enumerate(nomes))

print(lista_nomes_enumarados)

# A melhor forma de usar é assim

numeros = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

for indice, numero in enumerate(numeros):
    print(indice, numero)
