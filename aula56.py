"""
split -> divide uma string -> retorna uma lista
join -> une uma string
"""

frase = "Python é uma linguagem de programação."
outra_frase = "Mais uma vez, novamente."

lista_de_palavras_da_frase = frase.split()
lista_de_palavras_da_outra_frase = outra_frase.split(",")
uniao_outra_frase = ",".join(lista_de_palavras_da_outra_frase)

print(lista_de_palavras_da_frase)
print(lista_de_palavras_da_outra_frase)

for i, frase in enumerate(lista_de_palavras_da_frase):
    print(lista_de_palavras_da_frase[i])

for i, frase in enumerate(lista_de_palavras_da_outra_frase):
    print(
        lista_de_palavras_da_outra_frase[i].strip()
    )  # strip serve para cortar os espaços da direita e da esquerda e pode usar o lstrip para cortar so o da esquerda e rstrip para o da direita

print(uniao_outra_frase)
