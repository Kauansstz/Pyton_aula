"""
Constante = "Variáveis" que não vão mudar 
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade(ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada 

RADAR_1 = 60 #Velocidade máxima do radar 1 
LOCAL_1 = 100 # Local onde o radar 1 esta
RADAR_RANGER = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and  \
    local_carro <= (LOCAL_1 + RADAR_RANGER )

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

    if carro_multado_radar_1 and vel_carro_pass_radar_1:
        print('carro multado em radar 1') 