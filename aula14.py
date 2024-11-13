a = "a"
b = "b"
c = 1.5
string = "a={parametro1} b={parametro2} c={parametro3:.2f}"  # podemos chamar com o indice também, 0, 1, 2... ou deixar vazio que ele vai pegar na ordem
formato = string.format(parametro1=a, parametro2=b, parametro3=c)

print(formato)
