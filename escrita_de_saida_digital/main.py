"""
@brief Faz a alternancia de um pino 

Documentacao: https://docs.micropython.org/en/latest/library/machine.Pin.html
"""
from machine import Pin
import time

# define o pino #2 (LED) como saida
led = Pin(2, Pin.OUT)

while True:
    # liga o led
    led.on()
    print("Led ON")
    time.sleep(0.5) # aguarda 0.5 segundos

    # deslig ao led
    led.off()
    print("Led OFF")
    time.sleep(0.5) # aguarda 0.5 segundos
