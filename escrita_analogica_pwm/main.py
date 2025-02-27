"""
@brief Faz a escrita de um valor PWM em um pino do ESP

Documentacao: https://docs.micropython.org/en/latest/library/machine.PWM.html
"""
from machine import PWM, Pin
import time

# Inicializa um sinal PWM no pino 25
p2 = PWM(Pin(25))

while True:
    p2.duty_u16(0)  # seta o valor do PWM para 0 (0%)
                    # valores possiveis: 0 - 65535
    time.sleep(1)

    p2.duty_u16(32768) # seta o valor do PWM para 32768 (50%)
    time.sleep(1)

    # Variando o valor de 'i' de 0 a 65536, com passo de 1024 em 1024
    for i in range(0, 65536, 1024):
        print(f'Duty: {i}, ({100*float(i)/65535} %)')
        p2.duty_u16(i)
        time.sleep(.2)

