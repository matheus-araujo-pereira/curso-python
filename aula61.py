"""
Cálculo do 1° dígito do CPF

CPF: 063.189.135-80

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10.

Ex.: 10*0 + 9*6 + 8*3 + 7*1 + 6*8 + 5*9 + 4*1 + 3*3 + 2*5

Somar todos os resultados.

Multiplicar o resultado anterior por 10.

Obter o resto da divisão da conta anterior por 11.

Se o resultado anterior for maior que 9, o resultado é 0.

Caso contrário, o resultado é o valor da conta.
"""

cpf = "06318913580"
nove_digitos = cpf[0:9]
contador_regressivo = 10
resultado = 0

for digito_um in nove_digitos:
    resultado += int(digito_um) * contador_regressivo
    contador_regressivo -= 1

digito_um = resultado * 10 % 11
digito_um = digito_um if digito_um <= 9 else 0

print(digito_um)
