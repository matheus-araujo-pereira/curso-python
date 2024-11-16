"""
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este é par ou ímpar.
Caso o usuário não digite um múmero inteiro, informe que não é um número inteiro.
"""

mensagem = input("Digite um número INTEIRO: ")

if mensagem.isdigit():
    numero = int(mensagem)
    if numero % 2 == 0:
        print("PAR")
    else:
        print("ÍMPAR")
else:
    print("Não é um inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
"""

hora = int(input("Digite uma hora: "))

if 0 <= hora <= 11:
    print("Bom dia")
elif 12 <= hora <= 17:
    print("Boa tarde")
elif 18 <= hora <= 23:
    print("Boa noite")
else:
    print("Hora inválida.")

"""
Faça um programa que peça o 1° nome do usuário.
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto.".
Se tiver 5 ou 6, escreva "Seu nome é normal.".
Se maior que 6, escreva "Seu nome é muito grande.".
"""

nome = input("Digite o seu 1° nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto.")
elif tamanho_nome == 5 or tamanho_nome == 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
