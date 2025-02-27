"""
@brief Faz a leitura periodica de um pino do ESP

Documentacao: https://docs.micropython.org/en/latest/library/machine.Pin.html
"""
from machine import Pin

# define o pino #2 como entrada, Pull-up habilitado
p2 = Pin(2, Pin.IN, Pin.PULL_UP)

while True:
    # mostra o valor do pino #2 (1 como )
    print(f'Pino #2: {p2.value()}')