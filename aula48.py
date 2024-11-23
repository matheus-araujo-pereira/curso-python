"""
Listas

O tipo list é mutável.

Suporta valores de qualquer tipo.

Métodos úteis: append, insert, pop, del, clear, extend, +

Lista vazia retorna False.
"""

lista = [123, True, "Matheus", 1.0, ["outra lista", 456, False]]

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(type(lista))

print("Atualizando o nome...")

lista[2] = "Matheus Araujo Pereira"

print(lista)

print("Apagando o 4° item da lista...")

del lista[3]  # deleta o índice específico

print(lista)

lista.append("Tahiane")  # adiciona um item no final
lista.append("Ari")

print(lista)

lista.append("ULTIMO ELEMENTO")

print(lista)

lista.pop()  # remove o último item

print(lista)

lista.insert(
    0, "Meu nome é Matheus e vou inserir essa string no início da lista..."
)  # insere um item em um índice específico

print(lista)

lista.clear()  # limpar a lista

print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

print(lista_a)
print(lista_b)
print(lista_c)

primeira_lista = ["M", "A", "T"]
segunda_lista = ["H", "E", "U", "S"]

primeira_lista.extend(segunda_lista)  # adiciona os itens da 2° na 1° lista

print(primeira_lista)

terceira_lista = primeira_lista.copy()  # a 3° lista é uma cópia da 1°

print(terceira_lista)

"""
Cuidado com os dados mutáveis

= -> copiando o valor (imutável)
= -> aponta para o mesmo valor na memória (mutável)
"""

nome = "Matheus"
outro_nome = nome
nome = "Matheus Araujo"

print(nome)
print(outro_nome)  # continuou com o valor antigo de nome
