"""
@brief Faz a leitura periodica de um pino do ESP

Documentacao: https://docs.micropython.org/en/latest/library/machine.ADC.html
"""
from machine import ADC
import time

# define o pino #2 como entrada analogica
adc = ADC(2)

while True:
    print(f'Valor adc (0-65535) = {adc.read_u16()}')
    time.sleep(0.5)