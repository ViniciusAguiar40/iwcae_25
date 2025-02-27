"""
@file main.py
@brief Faz a conexao em uma rede Wi-Fi, se conecta a um broker MQTT e faz
       publicacoes em um topico
Documentacao: 
https://docs.micropython.org/en/latest/library/network.WLAN.html
https://mpython.readthedocs.io/en/v2.2.1/library/mPython/umqtt.simple.html
"""
import network
import time
from umqtt.simple import MQTTClient

# definicoes Wi-Fi
WIFI_SSID = 'WLL-Inatel'
WIFI_PASSWORD = 'inatelsemfio'

# definicoes MQTT
MQTT_BROKER = 'broker.emqx.io'
MQTT_CLIENT_ID = ''

MQTT_TOPIC = 'inatel_competence_center'

# Conexao Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
# Aguarda conexao
print("Connecting to Wi-Fi")
while not sta_if.isconnected():
    print('.', end = '')
    time.sleep(0.1)
print("Connected!")
# Conectado ao Wi-Fi

# Conexao com o broker MQTT
print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
client.connect()
print("Connected to MQTT")

contador = 0
# Loop infinito
while True:
    msg = f'Contando: {contador}'
    contador = contador + 1
    print(f'Publicando a mensagem: \"{msg}\" no topico \"{MQTT_TOPIC}\"')
    client.publish(MQTT_TOPIC, msg)
    time.sleep(1)
