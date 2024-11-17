frase = (
    "Três pratos de tigro para dez triges tistes e tem pero no pé do Pedro pelo no pé do preto."
).lower()

indice = 0
quantidade_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == " ":
        indice += 1
        continue

    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if quantidade_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        quantidade_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    indice += 1

print(
    f"A letra que mais apareceu foi {letra_apareceu_mais_vezes}, aparecendo {quantidade_apareceu_mais_vezes}x."
)
