# Conversão/Coerção de tipos

# Type convertion / Typecasting / Coercion é o ato de converter um tipo em outro

# Tipos imutáveis e primitivos: str, int, float e bool
print(1 + 2)
print(1.2 + 2.3)
print("a" + "b")
print("Math" + "eus")

# O python só vai fazer a conversão se for possível

print(int("1"), type(int("1")))
print(int("1") + 4)
print(bool(""))  # string vazia tem o valor False
print(bool(" "))  # string preenchida tem o valor True
print(str(11) + "b")
