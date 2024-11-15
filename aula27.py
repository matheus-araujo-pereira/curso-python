"""
Fatiamento de strings

Fatiamento [i:f:p] [::]

A função len retorna a quantidade de caracteres da str
"""

variavel = "matheus araujo pereira"
print(variavel[4:])
print(variavel[4:8])
print(variavel[:8])
print(variavel[14:20])
print(len(variavel[3]))
print(len(variavel[3:15]))
print(len(variavel[:15]))
print(len(variavel))
print(variavel[0 : len(variavel) : 1])
print(variavel[0:10:5])
print(variavel[::-1])
