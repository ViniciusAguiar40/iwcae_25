"""
@file main.py
@brief Faz a conexao em uma rede Wi-Fi, se conecta a um broker MQTT e se 
       inscreve em um topico
Documentacao: 
https://docs.micropython.org/en/latest/library/network.WLAN.html
https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple

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

MQTT_TOPIC = 'inatel_competence_center/#'

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

# Callback (funcao) que sera chamada em caso de mensagens
def message_callback(topic, msg):
    print(f'Message on topic {topic.decode()}')
    print(f'Message:{msg.decode()}')

# Define a funcao message_callback como funcao de callback de mensagens
client.set_callback(message_callback)

# Faz a inscricao no topico
client.subscribe(MQTT_TOPIC)

# Loop infinito
while True:
    # Espera uma mensagem
    if client.check_msg():
        print('Message received!')
