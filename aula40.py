# Calculadora com while

while True:
    print("Iniciando programa calculadora...")
    print("---------------------------------")

    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")

    operador = input("Digite o operador (+, -, / ou *) da operação desejada: ")

    numeros_validos = None
    float_numero_1 = 0
    float_numero_2 = 0

    try:
        float_numero_1 = float(numero_1)
        float_numero_2 = float(numero_2)

        numeros_validos = True
    except:
        numeros_validos = None
        print("A calculadora estourou um erro.")
        print("Reiniciando o sistema da calculadora...")

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos")
        print("Reiniciando o sistema da calculadora...")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        print("Reiniciando o sistema da calculadora...")
        continue

    if len(operador) > 1:
        print("Digite apenas 1 operador.")
        print("Reiniciando o sistema da calculadora...")
        continue

    print("Resultado da operação desejada:")

    if operador == "+":
        print(float_numero_1 + float_numero_2)
    elif operador == "-":
        print(float_numero_1 - float_numero_2)
    elif operador == "/":
        print(float_numero_1 / float_numero_2)
    elif operador == "*":
        print(float_numero_1 * float_numero_2)
    else:
        print("ESSA MENSAGEM NÃO DEVERIA APARECER")

    sair = (
        input("Deseja encerrar o programa? Digite s ou S para sair: ")
        .lower()
        .startswith("s")
    )

    if sair is True:
        break
