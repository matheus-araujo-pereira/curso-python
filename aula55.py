"""
Imprecisão de ponto flutuante

IEEE 754
"""

import decimal

n1 = decimal.Decimal("0.1")  # precisa colocar em string mesmo sendo float
n2 = decimal.Decimal("0.7")
n3 = n1 + n2

print(n3)
print(f"{n3:.2f}")
print(round(n3, 2))  # arrendondar as casa decimais
