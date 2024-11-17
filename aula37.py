contador = 0

while contador <= 100:
    contador += 1

    if contador == 2 or contador == 20:
        print("Não vou mostrar! °-°")
        continue  # volta pro while mais próximo

    print(contador)

    if contador == 40:
        break  # quebra a execução
