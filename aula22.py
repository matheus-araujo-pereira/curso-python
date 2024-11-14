# or -> qualquer condição verdadeira avalia toda a expressão como verdadeira
print(True or True or True)
print(True or True or False)  # Mesmo com o False, será True

entrada = input("[E]ntrar ou [S]air: ")
senha_digitada = input("Senha: ")

if (
    entrada == "E" or senha_digitada == "12345"
):  # Entra com a letra certa ou a senha certa, pelo menos 1 precisa ser verdadeira pra entrar
    print("Entrar")
elif entrada == "S":
    print("Sair")
else:
    print("Valor invalido")
