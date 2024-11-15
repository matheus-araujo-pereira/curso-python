"""
Interpolação básica de strings

s -> strings
d e i -> int
f -> float
x e X -> hexadecimal
"""

nome = "Matheus"
preco = 123.45
variavel = "%s, o preço é R$%.2f" % (nome, preco)

print(variavel)
