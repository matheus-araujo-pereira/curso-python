# Posso printar mais de 1 elemento
print(0)
print(1, 2, 3, 4)
print(5, 6, 7, 8)
print(9, 10)

# Separador
print(1, 2, 3, sep="    ")
print(10, 20, 30, sep='-')
print(400, 500, 600, sep='')
print(7000, 8000, 9000, sep='.')
print(100000, 110000, 1200000, sep=',')

# \r\n -> CRLF -> Windows
# \n -> LF -> Unix
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep=", ", end="\r\n")
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep=", ", end="\n")
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep=", ", end="Matheus\n")
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep=",\n", end="Matheus\n")