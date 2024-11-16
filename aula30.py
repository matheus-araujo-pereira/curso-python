"""
Constantes são variáveis que não vão mudar.

Usar letras maiúsculas para constantes.
"""

# constantes
VELOCIDADE_MAXIMA_RADAR_1 = 60  # será sempre esse valor, se precisar ser alterado, será alterado nessa mesma linha
LOCALIZACAO_RADAR_1 = "BR 101"  # será sempre esse valor, se precisar ser alterado, será alterado nessa mesma linha
MENSAGEM_CARRO_MULTADO = (
    "A velocidade do carro é maior que o limite estabelecido pelo radar. Carro multado!"
)

# variáveis
velocidade_atual_carro = 61  # velocidade atual do carro, pode mudar
localizacao_atual_carro = "BR 101"  # localização atual do carro, pode mudar
comparar_velocidade_carro_radar = velocidade_atual_carro > VELOCIDADE_MAXIMA_RADAR_1
comparar_localizacao_carro_radar = localizacao_atual_carro == LOCALIZACAO_RADAR_1


if comparar_velocidade_carro_radar and comparar_localizacao_carro_radar:
    print(MENSAGEM_CARRO_MULTADO)
