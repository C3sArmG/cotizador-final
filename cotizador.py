# cotizador.py
from datetime import datetime
import pandas as pd

def calcular_valor_kilometraje(kilometraje):
    if kilometraje <= 30000:
        return 250 
    elif kilometraje <= 60000:
        return 380  
    elif kilometraje <= 100000:
        return 470  
    else:
        return 650

def calcular_utilidad_estimada(pvp_mercado, rotacion):
    rango = [
        {"min": 1,    "max": 5000, "baja": 1800, "media": 1400, "alta": 1200},
        {"min": 5001, "max": 8000, "baja": 2000, "media": 1800, "alta": 1700},
        {"min": 8001, "max": 10000, "baja": 2400, "media": 2200, "alta": 2000},
        {"min": 10001, "max": 12000, "baja": 2800, "media": 2400, "alta": 2200},
        {"min": 12001, "max": 13500, "baja": 3000, "media": 2500, "alta": 2400},
        {"min": 13501, "max": 14500, "baja": 3200, "media": 2800, "alta": 2600},
        {"min": 14501, "max": 16000, "baja": 3500, "media": 3000, "alta": 2800},
        {"min": 16001, "max": 17500, "baja": 3800, "media": 3200, "alta": 3000},
        {"min": 17501, "max": 19000, "baja": 4000, "media": 3400, "alta": 3200},
        {"min": 19001, "max": 22500, "baja": 4500, "media": 3800, "alta": 3600},
        {"min": 22501, "max": 25000, "baja": 4800, "media": 4200, "alta": 4000},
        {"min": 25001, "max": 28000, "baja": 5000, "media": 4400, "alta": 4200},
        {"min": 28001, "max": 31000, "baja": 5200, "media": 4600, "alta": 4500},
        {"min": 31001, "max": 34500, "baja": 5900, "media": 5300, "alta": 5100},
        {"min": 34501, "max": 38500, "baja": 6400, "media": 5800, "alta": 5600},
        {"min": 38501, "max": 43000, "baja": 7100, "media": 6400, "alta": 6300},
        {"min": 43001, "max": 48000, "baja": 8000, "media": 7200, "alta": 7000}
    ]
    
    for r in rango:
        if r["min"] <= pvp_mercado <= r["max"]:
            return r[rotacion]
    

def cotizar_auto(pvp_mercado, kilometraje, rotacion):
    valor_por_kilometraje = calcular_valor_kilometraje(kilometraje)
    utilidad_estimada = calcular_utilidad_estimada(pvp_mercado, rotacion)
    valor_final = pvp_mercado - utilidad_estimada - valor_por_kilometraje
    return valor_final

def valor_partepago (valor_final):
    valor_partepago = valor_final * 1.028
    return valor_partepago

    
    
 

