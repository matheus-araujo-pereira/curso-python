"""
Operação ternária -> condicional de uma linha

valor if condicao else outro valor
"""

valor = 10
outro_valor = 11
condicao = valor == 10
variavel = valor if condicao else outro_valor

print(variavel)

numero = 7
novo_numero = numero if numero <= 9 else 0

print(novo_numero)

novo_numero = 0 if numero > 9 else numero

print(novo_numero)
