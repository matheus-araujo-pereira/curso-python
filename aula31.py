"""
Flag/Bandeira -> marcar um local
None -> não valor
is e is not -> é ou não é (tipo, valor, identidade)
id -> identidade
"""

n1 = "a"
n2 = "a"

print(id(n1))
print(id(n2))

if id(n1) == id(n2):
    print("Estão no mesmo local da memória.")
else:
    print("Não estão no mesmo local da memória.")

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Executando...")
else:
    print("Não está executando...")

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
