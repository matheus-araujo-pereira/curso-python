"""
Operadores lógicos:

and -> e
or -> ou
not -> não

No and, todas as condições precisam ser verdadeiras.

Os valores 0, 0.0, '', "" e False são considerados falsy/falsos.

Também existe o tipo none que é usado para representar um não valor.
"""

print(True and True and True)
print(True and True and False)  # Basta um valor False que não funcionará

entrada = input("[E]ntrar ou [S]air: ")
senha_digitada = input("Senha: ")

if entrada == "E" and senha_digitada == "12345":
    print("Entrar")
elif entrada == "S":
    print("Sair")
else:
    print("Valor invalido")
