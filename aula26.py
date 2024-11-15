"""
Formatação básica de string

s -> string
d -> int
f -> float
.(número de digitos)f
x ou X -> hexadecimal
> -> esquerda
< -> direita
^ -> centro
- ou + -> sinal
!r, !s e !a -> conversion flags
= -> força o número a aparecer antes dos zeros
"""

variavel = "ABD"

print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}")
print(f"{variavel: ^10}")
print(f"{1000000000000000:+,.2f}")
print(f"{variavel!r}")
