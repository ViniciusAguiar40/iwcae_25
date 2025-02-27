"""
@brief Faz a escrita de um valor PWM em um pino do ESP para controlar um servomotor
"""
import time
from servo import Servo

PINO_SERVO = 15

my_servo = Servo(PINO_SERVO)

while True:
    for x in range(0, 181, 30):
        my_servo.move(x)
        print(f'Angulo = {x}')
        time.sleep(2)

