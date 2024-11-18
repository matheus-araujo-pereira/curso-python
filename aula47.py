"""
Faça um jogo para o usuário advinhar qual a palavra secreta.

- Propor uma palavra secreta qualquer e dar a possibilidade para o usuário digitar apenas uma letra.
- Se a letra digitada estiver na palabra secreta, exiba a letra, se não estiver, exiba *.

Faça a contagem de tentativas do seu usuário e mostre-a quando acertar a palavra completa.
"""

import os

palavra_secreta = "matheus"
letras_acertadas = ""
numero_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")  # limpar o console
        print("Você conseguiu acertar a palavra secreta!")
        print("A palavra era:", palavra_secreta)
        print("Tentativas até o acerto:", numero_tentativas)
        break
