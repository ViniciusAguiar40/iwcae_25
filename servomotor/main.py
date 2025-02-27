"""
@brief Faz a escrita de um valor PWM em um pino do ESP para controlar um servomotor

Documentacao: https://docs.micropython.org/en/latest/library/machine.PWM.html
"""
from machine import PWM, Pin
import time

# Defina o pino onde o servo está conectado
pino_servo = 14  # Ajuste conforme necessário

# Configura o PWM no pino do servo
servo = PWM(Pin(pino_servo), freq=50)

def angulo_p_duty(angulo):
    # 0 - 2,5% - 1638.4
    # 180 - 12% - 8191.875
    duty = int((angulo*(8191.875-1638.4))/180+1638.4)
    return duty

# Exemplo de movimentação
while True:
    for i in range(0,181,5):
        v_duty = angulo_p_duty(i)
        if(v_duty > 0):
            servo.duty_u16(v_duty)
        print(f'Angulo: {i}, DC = {v_duty} = {float(v_duty)/65536*100} %')
        time.sleep(.2)