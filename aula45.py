"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = "Matheus Araujo Pereira"  # iterável
iterador = iter(texto)  # iterador

# o for faz isso em baixo dos panos
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in texto:
    print(letra)
