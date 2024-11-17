quantidade_de_linhas = 5
quantidade_de_colunas = 5

linha_atual = 1

while linha_atual <= quantidade_de_linhas:

    coluna_atual = 1

    while coluna_atual <= quantidade_de_colunas:

        print(linha_atual, coluna_atual)

        coluna_atual += 1

    linha_atual += 1

print("Finalizando...")
