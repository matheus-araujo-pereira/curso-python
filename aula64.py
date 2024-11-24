# Gerador de CPFs

import random

for documentos in range(100):
    nove_digitos = ""

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

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

    cpf = f"{nove_digitos}{digito_um}{digito_dois}"

    print(cpf)
