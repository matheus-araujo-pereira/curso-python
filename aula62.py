"""
Cálculo do 2° dígito do CPF

Colete a soma dos 9 primeiros dígitos do CPF mais o 1° dígito, multiplicando cada um dos valores por uma contagem regressiva começando de 11.

Somar todos os resultados.

Multiplicar o resultado anterior por 10.

Obter o resto da divisão da conta anterior por 11.

Se o resultado anterior for maior que 9, o resultado é 0.

Caso contrário, o resultado é o valor da conta.
"""

cpf = "06318913580"
nove_digitos = cpf[0:9]
contador_regressivo = 10
resultado_digito_um = 0

for digito_um in nove_digitos:
    resultado_digito_um += int(digito_um) * contador_regressivo
    contador_regressivo -= 1

digito_um = resultado_digito_um * 10 % 11
digito_um = digito_um if digito_um <= 9 else 0
dez_digitos = nove_digitos + str(digito_um)
contador_regressivo = 11
resultado_digito_dois = 0

for digito_dois in dez_digitos:
    resultado_digito_dois += int(digito_dois) * contador_regressivo
    contador_regressivo -= 1

digito_dois = resultado_digito_dois * 10 % 11
digito_dois = digito_dois if digito_dois <= 9 else 0

print(digito_um, digito_dois)
