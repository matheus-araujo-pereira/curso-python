# Introdução ao desempacotamento

nomes = ["Matheus", "Tahinae", "Ari"]  # mesma quantidade de item para variáveis
filho, mae, pai = nomes  # também pode passar a lista direto aqui

print(filho)
print(mae)
print(pai)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
um, dois, tres, quatro, cinco, *resto = (
    numeros  # juntando o resto em uma variável só com o *
)

print(um)
print(dois)
print(tres)
print(quatro)
print(cinco)
print(resto)
