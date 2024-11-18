"""
WHILE -> usado para quando não sabemos o número de repetições.
For -> usado para quando sabemos o número de repetições.
"""

senha_salva = "123456789"
senha_digitada = ""
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f"Sua senha ({repeticoes}x): ")
    repeticoes += 1

print(f"Foram {repeticoes} repetições até o acerto.")

texto = "Python é muito bom."
novo_texto = ""

for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)

print(novo_texto + "*")
