"""
try/except

try -> tenta executar
except -> ocorreu algum erro ao tentar executar
"""

numero_string = input("Vou dobrar o número digitado. Digite o número: ")

if numero_string.isdigit():
    print("STRING", numero_string)
    numero_float = float(numero_string)
    print("FLOAT", numero_float)
    print(f"O dobro de {numero_string} é {numero_float * 2:.2f}.")
else:
    print("Isso não é um número!")

print("----------Diferença entre usar o IF/ELSE e TRY/EXCEPT----------")

try:
    print("STRING", numero_string)
    numero_float = float(numero_string)
    print("FLOAT", numero_float)
    print(f"O dobro de {numero_string} é {numero_float * 2:.2f}.")
except:
    print("Isso não é um número!")
